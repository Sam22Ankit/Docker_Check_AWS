print("Hello World!")
token = "tW7jcc9BG5Q+VHvVwDxQw71CR9Vp0o3ZO7Ssv3Ks2/vFQtgwm3rrsDus6aPaCuzJ32S2Ey06U/0+DGrenhUdW5eXBsEqihiUb9+zl4opNJCy3SXvofbIg86HVtOviPnIeSyVgsDCIfhKHtHG+FphPuaZf9OXV23Q/BlVBWlkDbGyzSHcUulVpFjcsrn6tAMtS/POZvPTP0jq3lwUdPwMnket9DqtzqcLazpNuhdTJsG51wu8WNpjAiSqJ84JNrIF/WfffLTqNbVSxklxAAtM0W8SFEaNnhsuCmRXSHl8NJCt5e+LYvHMVllAQeJEwktFuGDZXKHELMMXZ8gqG2zCUGhkzw3g3DUaveFrOQwyG8bPN9X3t4nkrDCMkp2dzE/Si++Uu7xPrEiuDoX5zU9LuXEfl2OlqHxbeVguORzcs7dXAVUWySJI4+F+1GRaz6ldnhd12Fh28eK5lSniVYwvhoGo+qxpRdpMsnNV93sHeCwPvY9/0tf1HvQuOahzDk6buG0pbPbsNves0CBj5gz7nd/BTXy6LmopzCCSBvu2pj3YUgGxDVLDXxJxyarF+MiVtqq22ItdpSQq2aLTkWERCnCzgRZQiYfnDCqizmLoCybuHnF/hHW/6b3Z94zU0xyyPxRM44ydiKfczTDWud4ZS7We6N5XDax0OdN2kjJOarc="
alpha_token = "1RGLuV99JsM++H/htLRAMG94nEFEIsv7ZwGI2uSk"
print("Secure Token :" + token)
print("Alpha Numeric Key :" + alpha_token)
with open("cosign.key") as file:
  code = file.read()
print("Key is :"+ code)
