const createPushNotificationsJobs = (jobs, queue) => {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Process each job in the jobs array
  jobs.forEach((jobData, index) => {
    const job = queue.create('push_notification_code_3', jobData);

    job.on('enqueue', function() {
      console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', function() {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', function(err) {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on('progress', function(progress) {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    job.save();
  });
};

module.exports = createPushNotificationsJobs;
