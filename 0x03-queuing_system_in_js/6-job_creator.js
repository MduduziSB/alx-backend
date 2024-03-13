const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue();

// Create the object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message.'
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData);

job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
job.save();
