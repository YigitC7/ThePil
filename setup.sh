#!/bin/bash

sudo cp -r The-pil /usr/local/bin/the-pil
sudo cp pil-start_derlenmis /usr/local/bin/pil

sudo chmod +x /usr/local/bin/pil
sudo chmod -R +x /usr/local/bin/the-pil

sudo chown -R root:root /usr/local/bin/the-pil
sudo chown root:root /usr/local/bin/pil

echo "Başlatmak için 'pil' yazın."
