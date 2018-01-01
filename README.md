#To be changed

# 8bitdash

8bitdash is a start page for the browser (http://www.8bitdash.com/). The site shows outstanding pixel artworks. The artists gave permission to show their artworks on the site. Feel free to contribute features via pull-request.

## Clock

![Screenshot](http://i.imgur.com/YQe0UeC.jpg)

## Navigation

Scroll down, or press arrow down to swipe to the navigation part of the site. In the catalog you will find useful sites and interesting sites to start your day.

![Alt](http://i.imgur.com/wcOgXwL.png?1)

## Preparing Environment To Make Changes

To make custom changes you will need to have python installed along with jscssmin. To do this follow the instructions below.

##### Ubuntu/Debian

  1. Run the following commands in Ubuntu or Debian to install Python and jscssmin
  
      ```
      sudo apt-get install python-pip python-dev build-essential
      sudo pip install --upgrade pip
      sudo pip install --upgrade virtualenv
      sudo pip install jscssmin
      ```

##### Windows

  1. Download the latest Python 2.7 from [here](https://www.python.org/downloads/release/python-2710/). 
  
  2. Install the python-setup tools package by right clicking [this](https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py) link and save it as ez_setup.py. Once it is downloaded right click the file and select open with IDLE and press F5 when it opens to run the script.
  
  3. Use the same process as above to install the python package manager pip from [this](https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py) link and save it as pip.py and then run it as above.
  
  4. The final step is to open a command prompt by going to your Windows search menu or run menu and typing cmd. Once the command prompt opens run the following command to install jscssmin.
  
  ```
  pip install jscssmin --target $PYTHONPATH --install-option="--install-scripts=~/bin"
  ```

## Customizing Links

To add your own links follow the steps below.

  1. Go into the js folder and open links.js
  2. Make changes to links or categories
  3. Save the file
  4. Go into the scripts folder and run compile.py using the commands below
  
    **Ubuntu/Debian**

    ```
    sudo python compile.py
    ```
    
    **Windows**
    
    Open command prompt in the folder where compile.py is located by shift right clicking in a blank area and select open command prompt here. Run the command below.
    
    ```
    python compile.py
    ```
    
  5. Your dash site should be modified. Open it with a web browser to check the changes.

## Contributors

* Jendrik Poloczek [@madewithtea](https://twitter.com/madewithtea) (Idea, programming and artist relations)
* José Luis Bonilla [@DJBlayOfficial](https://twitter.com/DJBlayOfficial) (Language feature)

## Pixel Artists

Check out the credit section below on the site. 
