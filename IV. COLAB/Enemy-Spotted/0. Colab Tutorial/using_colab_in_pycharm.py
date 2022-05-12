# Reference: https://engineer-mole.tistory.com/227

import subprocess
import pprint


DEFAULT_ATTRIBUTES = (
    'index', 'uuid', 'name', 'timestamp', 'memory.total', 'memory.free', 'memory.used', 'utilization.gpu',
    'utilization.memory')


def get_gpu_info(nvidia_smi_path='nvidia-smi', keys=DEFAULT_ATTRIBUTES, no_units=True):
    nu_opt = '' if not no_units else ',nounits'
    cmd = '%s --query-gpu=%s --format=csv,noheader%s' % (nvidia_smi_path, ','.join(keys), nu_opt)
    output = subprocess.check_output(cmd, shell=True)
    lines = output.decode().split('\n')
    lines = [line.strip() for line in lines if line.strip() != '']
    return [{k: v for k, v in zip(keys, line.split(', '))} for line in lines]


pprint.pprint(get_gpu_info())
