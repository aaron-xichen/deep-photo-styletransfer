# deep-photo-styletransfer
Fork from [deep-photo-styletransfer](https://github.com/luanfujun/deep-photo-styletransfer)

## Modification
- Remove redundancy in examples
- Add `-v6` flag in gen_laplacian.m when using octave

## Detail Instructions
### Installation
- Install Octave 
```
sudo apt-get install octave
sudo apt-get install octave-control octave-image octave-io octave-optim octave-signal octave-statistics

```

- Install torch
```
git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch; 
bash install-deps; # maybe skip 
./install.sh
sudo apt-get install libmatio2
luarocks install matio
luarocks install loadcaffe
```

- Download pre-trained VGG-19 model
```
sh models/download_models.sh
```

- Compile extra cuda lib (Modify the first two lines in makefile, then make it)
```
make clean && make
```

### Running

- Please make sure the all png images has longer side less than 700px, [resize_images.py](resize_images.py) will help to do that.

-  Generate laplacian matrix (Takes really long, matlab is faster)
```
cd gen_laplacian;
octave gen_laplacian.m --no-gui
```

- Masks with the same color is in the same group.
- Ok let's go
```
python gen_all.py
```

- Test successfully on TITAN X with 12GB memory, no OOM issues.
