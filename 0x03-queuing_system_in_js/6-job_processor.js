const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue();

// Define the function to send notifications
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber},`,
    'with message:',
    message,
  );
};

// Process jobs in the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  
  sendNotification(phoneNumber, message);
  done();
});
