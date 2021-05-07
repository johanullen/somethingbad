import subprocess
import logging
import yaml
import json

def something(cronjob_path, dry_run):
    cronjob_def = yaml.full_load(open(cronjob_path))
    cmd = ['kubectl', '-n', 'data-platform', 'apply', '-f', '-']
    conf = json.dumps(cronjob_def)
    logging.info(cmd)
    logging.info(conf)
    SubprocessHelper.run(cmd, input = json.dumps(cronjob_def), encoding='utf-8', check=True)
  
class SubprocessHelper():
    @staticmethod
    def run(cmd, *args, **kwargs):
        logging.info(f"+ {" ".join([str(c) for c in cmd])}")
        res = subprocess.run(cmd, *args, **kwargs)
        res.check_returncode()
        return res
