# sitechecker
A website deadoralive checker

1. `sitechecker.py` checks a single site. A basic program
2. `multichecker.py` checks a near infinite number of sites quickly using threading
3. `runner.sh` intended to be run using cron

## Example Cron Line: 
`*/1 * * * * /home/ubuntu/github/augurlabs/sitechecker/runner.sh >> /home/ubuntu/github/augurlabs/sitechecker/cron.log` will run it every minute
