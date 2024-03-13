const createPushNotificationsJobs = require('./8-job');
const kue = require('kue');

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue({ redis: { port: 6379, host: '127.0.0.1' } });
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue))
      .toThrow('Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Message 1' },
      { phoneNumber: '4153518781', message: 'Message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).toBe(2);
  });

  it('should handle job creation, completion, failure, and progress', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Message 1' },
      { phoneNumber: '4153518781', message: 'Message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).toBe(2);

    queue.testMode.jobs[0].emit('complete');
    queue.testMode.jobs[1].emit('complete');

    expect(console.log).toHaveBeenCalledWith('Notification job completed');
    expect(console.log).toHaveBeenCalledWith('Notification job completed');

    queue.testMode.jobs[0].emit('failed', new Error('Job failed'));
    queue.testMode.jobs[1].emit('failed', new Error('Job failed'));

    expect(console.log).
      toHaveBeenCalledWith('Notification job failed: Error: Job failed');
    expect(console.log).
      toHaveBeenCalledWith('Notification job failed: Error: Job failed');

    queue.testMode.jobs[0].emit('progress', 50);
    queue.testMode.jobs[1].emit('progress', 25);

    // Verify job progress
    expect(console.log).toHaveBeenCalledWith('Notification job 0 50% complete');
    expect(console.log).toHaveBeenCalledWith('Notification job 1 25% complete');
  });
});
