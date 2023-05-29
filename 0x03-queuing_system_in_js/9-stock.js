import express from 'express';
import { promisify } from 'util';
import { createClient as createRedisClient } from 'redis';

const productList = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    initialQuantity: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    initialQuantity: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    initialQuantity: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    initialQuantity: 5
  },
];

const getProductById = (id) => {
  const product = productList.find(obj => obj.id === id);

  if (product) {
    return Object.fromEntries(Object.entries(product));
  }
};

const app = express();
const redisClient = createRedisClient();
const PORT = 1245;

/**
 * Modifies the reserved stock for a given product.
 * @param {number} productId - The id of the product.
 * @param {number} stock - The stock of the product.
 */
const reserveStockById = async (productId, stock) => {
  return promisify(redisClient.SET).bind(redisClient)(`product.${productId}`, stock);
};

/**
 * Retrieves the reserved stock for a given product.
 * @param {number} productId - The id of the product.
 * @returns {Promise<String>}
 */
const getCurrentReservedStockById = async (productId) => {
  return promisify(redisClient.GET).bind(redisClient)(`product.${productId}`);
};

app.get('/products', (_, res) => {
  res.json(productList);
});

app.get('/products/:productId(\\d+)', (req, res) => {
  const productId = Number.parseInt(req.params.productId);
  const product = getProductById(Number.parseInt(productId));

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }
  getCurrentReservedStockById(productId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
      product.currentQuantity = product.initialQuantity - reservedStock;
      res.json(product);
    });
});

app.get('/reserve_product/:productId', (req, res) => {
  const productId = Number.parseInt(req.params.productId);
  const product = getProductById(Number.parseInt(productId));

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }
  getCurrentReservedStockById(productId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
      if (reservedStock >= product.initialQuantity) {
        res.json({ status: 'Not enough stock available', productId });
        return;
      }
      reserveStockById(productId, reservedStock + 1)
        .then(() => {
          res.json({ status: 'Reservation confirmed', productId });
        });
    });
});

const resetProductStock = () => {
  return Promise.all(
    productList.map(
      product => promisify(redisClient.SET).bind(redisClient)(`product.${product.id}`, 0),
    )
  );
};

app.listen(PORT, () => {
  resetProductStock()
    .then(() => {
      console.log(`API available on localhost port ${PORT}`);
    });
});

export default app;
