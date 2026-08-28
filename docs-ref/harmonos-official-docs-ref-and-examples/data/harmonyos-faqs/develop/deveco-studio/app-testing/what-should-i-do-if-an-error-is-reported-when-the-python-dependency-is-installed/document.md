# What should I do if an error is reported when the Python dependency is installed in DevEco Studio AppAnalyzer?

**Symptom**

An error is reported when the Python dependency is installed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/B-rLTqA3Q5KvsJ1QZWBNHg/en-us_image_0000002265289721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79166C646551C55CA60D06E278C3E3A8F519F89C64A87FF3561A9F04BB13CE2D)

**Possible Cause 1**

The pip configuration is incorrect.

**Solution**

1.  Modify the pip configuration.
    
    The pip configuration file is located at the user's root directory: **~/.pip/pip.conf** (**C:\\Users\\<UserName>\\pip\\pip.ini\*** on Windows). You can configure it as follows:
    
    \[global\]
    index-url = https://mirrors.huaweicloud.com/repository/pypi/simple
    trusted-host = mirrors.huaweicloud.com
    timeout = 120 
    
    If you need to set a proxy, refer to the following configuration. If **username** and **password** contain special characters, escape them. Change the values of **proxyserver** and **port** based on the actual proxy server. Perform the following steps:
    
    \[global\]
    index-url = https://mirrors.huaweicloud.com/repository/pypi/simple
    proxy = http://username:password@proxyserver:port/
    trusted-host = mirrors.huaweicloud.com
    timeout = 120  
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/_LVbCrfDQaWPd1a72cV_iw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACA291B3D8E7F6FD68EA8128BC7B88A021DBDA900AE98361E447C8EBB0424E8A)
    
    If the password contains special characters, such as @, #, and \*, the configuration may not take effect. In this case, you are advised to replace the special characters with ASCII codes and add a percent sign (%) before the ASCII codes. Refer to the following for the mapping between common symbols and ASCII codes:
    
    -   !: %21
    -   @: %40
    -   #: %23
    -   $: %24
    -   &: %26
    -   \*: %2A
    
2.  View the current pip configuration.
    
    pip config list
    

**Possible Cause 2**

The installation directory of Python is not deleted when Python is uninstalled on Windows.

**Solution**

Delete the Python installation directory.

**Possible Cause 3**

There is an issue with the Internet connection.

**Solution**

Cold start, white block detection, and UX test require network connection to download dependencies. Change the network with Internet access.

**Possible Cause 4**

PaddlePaddle==2.6.1 has been sunset, resulting in failed pip installation.

**Solution**

macOS

 //Access the Python installation directory.
cd python\_dir\_xxxx   
//Python 3.9 installation command
./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp39-cp39-macosx\_10\_9\_x86\_64.whl
//Python 3.10 installation command
./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp310-cp310-macosx\_10\_9\_x86\_64.whl
//Python 3.11 installation command
./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp311-cp311-macosx\_10\_9\_x86\_64.whl
//Python 3.12 installation command
./python -m pip install https://paddle-wheel.bj.bcebos.com/2.6.1/macos/macos-cpu-openblas/paddlepaddle-2.6.1-cp312-cp312-macosx\_10\_9\_x86\_64.whl

Windows

//Access the Python installation directory.
cd python\_dir\_xxxx   
./python.exe -m pip install paddlepaddle==2.6.1 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

**Possible Cause 5**

There is an issue with Python compatibility.

**Solution**

Python is incompatible with the dependencies of some specified versions. The supported versions are Python 3.9 to 3.12. Python 3.11.7 is recommended. If the latest Python version is incompatible with some dependencies, you are advised to uninstall Python and install the recommended version or update [DevEco Studio](https://developer.huawei.com/consumer/en/deveco-studio/).

<table><tbody><tr><td class="cellrowborder" valign="top" width="20%"><p>Category</p></td><td class="cellrowborder" valign="top" width="20%"><p>Third-Party Library</p></td><td class="cellrowborder" valign="top" width="20%"><p>DevEco Studio 5.0.x</p></td><td class="cellrowborder" valign="top" width="20%"><p>DevEco Studio 5.1.x</p></td><td class="cellrowborder" valign="top" width="20%"><p>DevEco Studio 6.0.x</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start &amp;&amp; White Block Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>Flask</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.3</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.3</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.3</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start &amp;&amp; White Block Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>numpy</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start &amp;&amp; White Block Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>onnxruntime</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.19.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.19.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.19.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start &amp;&amp; White Block Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>opencv-python</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start &amp;&amp; White Block Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>pillow</p></td><td class="cellrowborder" valign="top" width="20%"><p>10.4.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>10.4.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>10.4.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start &amp;&amp; White Block Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>pyclipper</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0.post6</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0.post6</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0.post6</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start &amp;&amp; White Block Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>shapely</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.0.6</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.0.6</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.0.6</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start &amp;&amp; White Block Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>waitress</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.0.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>hypium</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>xdevice</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>xdevice-devicetest</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>xdevice-ohos</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.0.7.200</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>loguru</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.7.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.7.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>numpy</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>stable_baselines3</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.3.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.3.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>gym</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.26.2</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.26.2</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>gym-notices</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.0.8</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.0.8</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>gymnasium</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.29.1</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.29.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>Shimmy</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.3.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>opencv-python</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>cffi</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.17.1</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.17.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>pynacl</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.5.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.5.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>torch</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p><p></p></td><td class="cellrowborder" valign="top" width="20%"><p>Python version &lt; 3.12: 2.0.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>Python version &lt; 3.12: 2.0.0</p><p>Python version == 3.12: 2.2.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>torchaudio</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p><p></p></td><td class="cellrowborder" valign="top" width="20%"><p>Python version &lt; 3.12: 2.0.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>Python version &lt; 3.12: 2.0.0</p><p>Python version == 3.12: 2.2.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>torchvision</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p><p></p></td><td class="cellrowborder" valign="top" width="20%"><p>Python version &lt; 3.12: 0.15.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>Python version &lt; 3.12: 0.15.0</p><p>Python version == 3.12: 0.17.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Cold Start - Automatic</p></td><td class="cellrowborder" valign="top" width="20%"><p>setuptools</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>Python version &lt; 3.12: Included with Python</p><p>Python version == 3.12: 80.9.0</p></td><td class="cellrowborder" valign="top" width="20%"><p>Python version &lt; 3.12: Included with Python</p><p>Python version == 3.12: 80.9.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Foldable Device UX Rule Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>numpy</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.26.4</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Foldable Device UX Rule Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>ImageHash</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.3.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Foldable Device UX Rule Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>opencv-python</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>4.10.0.84</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Foldable Device UX Rule Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>paddlepaddle</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>Python version &lt; 3.12: 2.6.2</p><p>Python version == 3.12: 3.0.0</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Foldable Device UX Rule Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>paddleocr</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>2.8.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Foldable Device UX Rule Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>psutil</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>5.9.8</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Foldable Device UX Rule Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>Werkzeug</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>3.1.3</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Foldable Device UX Rule Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>scikit-learn</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>1.5.1</p></td></tr><tr><td class="cellrowborder" valign="top" width="20%"><p>Foldable Device UX Rule Detection</p></td><td class="cellrowborder" valign="top" width="20%"><p>supervision</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>NA</p></td><td class="cellrowborder" valign="top" width="20%"><p>0.17.1</p></td></tr></tbody></table>
