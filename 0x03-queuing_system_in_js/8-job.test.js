import { createPushNotificationsJobs } from './pushNotificationUtils';
import { Queue, Job } from 'kue';

describe('createPushNotificationsJobs', () => {
  let queue;
  let createJobSpy;

  beforeEach(() => {
    queue = new Queue();
    createJobSpy = jest.spyOn(queue, 'create');
  });

  afterEach(() => {
    createJobSpy.mockRestore();
  });

  it('should create push notification jobs for each job info', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(createJobSpy).toHaveBeenCalledTimes(2);
    expect(createJobSpy).toHaveBeenNthCalledWith(1, 'push_notification_code_3', jobs[0]);
    expect(createJobSpy).toHaveBeenNthCalledWith(2, 'push_notification_code_3', jobs[1]);
  });

  it('should throw an error if jobs is not an array', () => {
    const invalidJobs = 'not an array';

    expect(() => {
      createPushNotificationsJobs(invalidJobs, queue);
    }).toThrow('Jobs is not an array');

    expect(createJobSpy).not.toHaveBeenCalled();
  });

  it('should attach event listeners to the created jobs', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(createJobSpy).toHaveBeenCalledTimes(1);
    expect(createJobSpy).toHaveBeenCalledWith('push_notification_code_3', jobs[0]);

    const createdJob = createJobSpy.mock.results[0].value;
    expect(createdJob.on).toHaveBeenCalledTimes(4);
    expect(createdJob.save).toHaveBeenCalledTimes(1);
  });
});
