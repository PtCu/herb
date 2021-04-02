#include <dht11.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x20, 16, 2);
dht11 DHT;
#define DHT11_PIN 4
boolean readCompleted = false;
String serialString = "";
boolean open[4];

void setup()
{
  Serial.begin(9600);
  serialString.reserve(200);
}

void loop()
{
  int chk = DHT.read(DHT11_PIN);
  int ligt_intensity;
  ligt_intensity = analogRead(0);
  //从传感器读取数据到串口
  int flameSensor = analogRead(1);
  Serial.print(DHT.temperature, 1);
  Serial.print('|');
  Serial.print(DHT.humidity, 1);
  Serial.print('|');
  Serial.print(ligt_intensity, 1);
  Serial.print('|');
  Serial.print(flameSensor, 1);
  Serial.print('\n');

  //保证原子操作。从串口读取服务器发来的数据
  if (readCompleted)
  {
    bool open_temper = serialString[0] - '0';
    bool open_humi = serialString[1] - '0';
    bool open_light = serialString[2] - '0';
    bool open_press = serialString[3] - '0';
    if (open_temper)
    {
      //TODO:开启加热装置
      Serial.print("heat\n");
    }
    if (open_humi)
    {
      //TODO:开启加热装置
      Serial.print("humi\n");
    }
    if (open_light)
    {
      //TODO:开启加热装置
      Serial.print("light\n");
    }
    if (open_press)
    {
      //TODO:开启加热装置
      Serial.print("press\n");
    }
    readCompleted = false;
  }
  delay(500);
}
void serialEvent()
{
  int i = 0;
  while (Serial.available())
  {
    char inChar = (char)Serial.read();
    if (inChar != '\n')
    {
      if (inChar != '|')
        open[i++] = inChar - '0';
    }
    else
      readCompleted = true;
  }
}
