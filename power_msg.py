from subprocess import Popen, PIPE

with open("/sys/class/power_supply/BAT1/energy_now") as f:
    charge_now = float(f.read())
with open("/sys/class/power_supply/BAT1/energy_full") as f:
    charge_full = float(f.read())
with open("/sys/class/power_supply/BAT1/status") as f:
    status = str(f.readline().rstrip())

percent = 100*charge_now/charge_full

if percent < 10 and status == "Discharging":
    p = Popen(['osd_cat','-A','center','-p','top','-f','-*-*-bold-*-*-*-60-*-*-*-*-*-*-*','-d','4','-s','200'],stdin=PIPE)
    p.communicate(input=b"Battery Low!")
    p.wait()
