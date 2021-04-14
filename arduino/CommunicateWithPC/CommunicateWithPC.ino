#include <dht11.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x20, 16, 2);
dht11 DHT;
#define DHT11_PIN 4
boolean readCompleted = false;
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
    if (open[0])
    {
      //TODO:开启加热装置
      Serial.print("heat\n");
    }
    if (open[1])
    {
      //TODO:开启加热装置
      Serial.print("humi\n");
    }
    if (open[2])
    {
      //TODO:开启加热装置
      Serial.print("light\n");
    }
    if (open[3])
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
