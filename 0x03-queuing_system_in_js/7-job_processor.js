import { createQueue as createNewQueue, Job as NewJob } from 'kue';

const NEW_BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];
const newQueue = createNewQueue();

/**
 * Sends a push notification to a user.
 * @param {String} newPhoneNumber
 * @param {String} newMessage
 * @param {NewJob} newJob
 * @param {*} newDone
 */
const sendNewNotification = (newPhoneNumber, newMessage, newJob, newDone) => {
  let newTotal = 2, newPending = 2;
  let newSendInterval = setInterval(() => {
    if (newTotal - newPending <= newTotal / 2) {
      newJob.progress(newTotal - newPending, newTotal);
    }
    if (NEW_BLACKLISTED_NUMBERS.includes(newPhoneNumber)) {
      newDone(new Error(`Phone number ${newPhoneNumber} is blacklisted`));
      clearInterval(newSendInterval);
      return;
    }
    if (newTotal === newPending) {
      console.log(
        `Sending notification to ${newPhoneNumber},`,
        `with message: ${newMessage}`,
      );
    }
    --newPending || newDone();
    newPending || clearInterval(newSendInterval);
  }, 1000);
};

newQueue.process('push_notification_code_2', 2, (newJob, newDone) => {
  sendNewNotification(newJob.data.phoneNumber, newJob.data.message, newJob, newDone);
});
