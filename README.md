# sitechecker
A website deadoralive checker

1. `sitechecker.py` checks a single site. A basic program
2. `multichecker.py` checks a near infinite number of sites quickly using threading
3. `runner.sh` intended to be run using cron

## Example Cron Line: 
`*/1 * * * * /home/ubuntu/github/augurlabs/sitechecker/runner.sh >> /home/ubuntu/github/augurlabs/sitechecker/cron.log` will run it every minute

## Slack Configuration
1. Start Here: https://api.slack.com/start
2. You need to create an app, and generate an app token that has permissions to create a chat message
3. The required channel ID can be obtained by right clicking on a channel. You likely need admin rights on the Slack org to make this work https://slack.dev/python-slack-sdk/installation/index.html#access-tokens
4. Export the slack application token as an environment variable, and add that variable to the default .bashrc, .profile. .zshrc or other shell environment setup configuratoin of your choosing. `export SLACK_TOKEN='my-slack-app-token'` or something similar. 
