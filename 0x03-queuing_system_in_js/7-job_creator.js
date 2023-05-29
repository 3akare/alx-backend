import { createQueue as createNewQueue } from 'kue';

const newJobs = [
  {
    newPhoneNumber: '4153518780',
    newMessage: 'This is the code 1234 to verify your account',
  },
  {
    newPhoneNumber: '4153518781',
    newMessage: 'This is the code 4562 to verify your account',
  },
  {
    newPhoneNumber: '4153518743',
    newMessage: 'This is the code 4321 to verify your account',
  },
  {
    newPhoneNumber: '4153538781',
    newMessage: 'This is the code 4562 to verify your account',
  },
  {
    newPhoneNumber: '4153118782',
    newMessage: 'This is the code 4321 to verify your account',
  },
  {
    newPhoneNumber: '4153718781',
    newMessage: 'This is the code 4562 to verify your account',
  },
  {
    newPhoneNumber: '4159518782',
    newMessage: 'This is the code 4321 to verify your account',
  },
  {
    newPhoneNumber: '4158718781',
    newMessage: 'This is the code 4562 to verify your account',
  },
  {
    newPhoneNumber: '4153818782',
    newMessage: 'This is the code 4321 to verify your account',
  },
  {
    newPhoneNumber: '4154318781',
    newMessage: 'This is the code 4562 to verify your account',
  },
  {
    newPhoneNumber: '4151218782',
    newMessage: 'This is the code 4321 to verify your account',
  },
];

const newQueue = createNewQueue({ name: 'push_notification_code_2' });

for (const newJobInfo of newJobs) {
  const newJob = newQueue.create('push_notification_code_2', newJobInfo);

  newJob
    .on('enqueue', () => {
      console.log('Notification job created:', newJob.id);
    })
    .on('complete', () => {
      console.log('Notification job', newJob.id, 'completed');
    })
    .on('failed', (err) => {
      console.log('Notification job', newJob.id, 'failed:', err.message || err.toString());
    })
    .on('progress', (progress, _data) => {
      console.log('Notification job', newJob.id, `${progress}% complete`);
    });
  newJob.save();
}
