## Run ocean.py on your computer which send trash plastic images to a server, and from https://oceanplastic.herokuapp.com you can see images.

```python
python ocean.py <token>   # run this command to detect plastic near camera 
```

```python
python ocean.py <token> < file_name.mp4 >   # run this command to detect plastic from < file_name.mp4 > 
```
## For example :
```python
python ocean.py fjkffdhbhdbhjdbhjdvhjdvjg56565 plastic.mp4   # run this command to detect plastic from < file_name.mp4 > 
```

## How to got the token ?

Login and go to https://oceanplastic.herokuapp.com/get_token/

![image](https://user-images.githubusercontent.com/55041104/196272343-91818455-920d-484a-adcb-3f46b951624d.png)


## Limitations for external users

To upload video or image you must have credentials. We don't allow external users to register our website, as this prototype allows images from their organizations.