# Installation
```bash
pip install git+https://github.com/oqx4579s/keyboard_pub.git \
&& mkdir -p /home/$USER/.config/systemd/user/ \
&& echo "[Unit]\nDescription=Keyboard Pub\n\n[Service]\nExecStart=/usr/bin/python3 $(python3 -c 'import keyboard_pub; print(keyboard_pub.__path__[0])')\nRestart=always\n\n[Install]\nWantedBy=graphical-session.target" \
> /home/$USER/.config/systemd/user/keyboard_pub.service \
&& systemctl --user daemon-reload \
&& systemctl --user enable keyboard_pub \
&& systemctl --user start keyboard_pub \
&& systemctl --user status keyboard_pub \
&& ip a
```