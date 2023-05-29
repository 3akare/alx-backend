import { Queue as NewQueue, Job as NewJob } from 'kue';

/**
 * Creates push notification jobs from the array of jobs info.
 * @param {NewJob[]} newJobs
 * @param {NewQueue} newQueue
 */
export const createNewPushNotificationsJobs = (newJobs, newQueue) => {
  if (!(newJobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const newJobInfo of newJobs) {
    const newJob = newQueue.create('push_notification_code_3', newJobInfo);

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
};

export default createNewPushNotificationsJobs;
