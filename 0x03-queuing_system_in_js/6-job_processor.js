import { createQueue as createNewQueue } from 'kue';

const newQueue = createNewQueue();

const sendNotification = (newPhoneNumber, newMessage) => {
  console.log(
    `Sending notification to ${newPhoneNumber},`,
    'with message:',
    newMessage,
  );
};

newQueue.process('push_notification_code', (newJob, done) => {
  sendNotification(newJob.data.phoneNumber, newJob.data.message);
  done();
});
