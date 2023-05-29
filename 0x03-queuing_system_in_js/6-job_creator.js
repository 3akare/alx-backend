import { createQueue as createNewQueue } from 'kue';

const newQueue = createNewQueue({name: 'push_notification_code'});

const newJob = newQueue.create('push_notification_code', {
  phoneNumber: '07045679939',
  message: 'Account registered',
});

newJob
  .on('enqueue', () => {
    console.log('Notification job created:', newJob.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
newJob.save();
