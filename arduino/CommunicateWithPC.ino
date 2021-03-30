#include <dht11.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x20,16,2);
dht11 DHT;
#define DHT11_PIN 4
boolean readCompleted = false;
String serialString = "";
String set[4];
void setup() {
  Serial.begin(9600);
  serialString.reserve(200);
}

void loop() {
  int chk= DHT.read(DHT11_PIN);
  int LIGHT_PIN;
  LIGHT_PIN=analogRead(0);
  //从传感器读取数据到串口
  int flameSensor = analogRead(1);
  Serial.print(DHT.temperature,1);Serial.print("|");
  Serial.print(DHT.humidity,1);Serial.print("|");
  Serial.print(LIGHT_PIN,1);Serial.print("|");
  Serial.print(flameSensor,1);Serial.print("|");

  //保证原子操作。从串口读取服务器发来的数据
  if (readCompleted) {
    int i = 0;
    //整理数据至serialstring
    while (serialString.length() > 0) {
      int index = serialString.indexOf('|');
      if (index != -1) {
        set[i++] = serialString.substring(0, index);
        //这个substring和c++的不一样。to也是下标
        serialString = serialString.substring(index + 1, serialString.length());
        //Serial.println(serialString);
      }
      else {
        if (serialString.length() > 0){
          set[i] = serialString;
          serialString = "";
        }
      }
    }
    //why start from 2?
    serialString+=set[2];serialString+="|";
    serialString+=set[3];
    //Serial.println(serialString);
    serialString = "";
    readCompleted = false;
  }
  delay(100);
}
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar != '\n')
      serialString += inChar;
    else
      readCompleted = true;
  }
}
