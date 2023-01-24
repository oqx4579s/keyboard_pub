# Installation
```bash
pip install git+https://github.com/oqx4579s/keyboard_pub.git \
&& mkdir -p /home/$(whoami)/.config/systemd/user/ \
&& echo "[Unit]\nDescription=Keyboard Pub\n\n[Service]\nExecStart=$(python3 -c 'import sys, keyboard_pub; print(sys.executable, keyboard_pub.__path__[0])')\nRestart=always\n\n[Install]\nWantedBy=graphical-session.target" \
> /home/$(whoami)/.config/systemd/user/keyboard_pub.service \
&& systemctl --user daemon-reload \
&& systemctl --user enable keyboard_pub \
&& systemctl --user start keyboard_pub \
&& systemctl --user status keyboard_pub \
&& ip a
```