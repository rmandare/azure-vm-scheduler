# Azure VM Scheduler

Starts and stops dev VMs on a schedule. Runs as a cron job on my home server.

Saves ~60% on my Azure dev VM costs by shutting them down outside work hours.

## Usage

```bash
pip install -r requirements.txt
python scheduler.py --action stop
python scheduler.py --action start
```

## TODO

- [ ] Move credentials to Key Vault
- [ ] Add tag-based filtering (only VMs tagged `auto-shutdown=true`)
- [ ] Slack notification on action
