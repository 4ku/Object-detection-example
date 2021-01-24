# Object detection with Tensofrlow API  

## Installation  
First of all you need Linux machine with `Python3.7`. Than do next steps:  
1. Go to project repository and create a virtual environment.  
    ```sh
    virtualenv env
    env/bin/activate
    ```
2. Run installation script
    ```sh
    chmod +x prepare.sh
    ./prepare.sh
    ```

## Launch  
Run with default parameters
```sh
python recognition
```  
More general way  
```sh
python recognition --path path/to/video/file --model model_name
```  
For more information use help  
```sh
python recognition -h
```  