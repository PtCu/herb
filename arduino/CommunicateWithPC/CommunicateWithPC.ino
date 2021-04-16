#include <dht11.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x20, 16, 2);
dht11 DHT;
#define LIGHT_PIN 0
#define FLAME_PIN 1
#define DHT11_PIN 2

#define HEAT_PIN 1
#define HUMI_PIN 3
#define LIGHT_PIN 5
#define PRESS_PIN 7

boolean readCompleted = false;
boolean open[4];
int ledPin = 3; // LED connected to digital pin 3
void setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  int chk = DHT.read(DHT11_PIN);
  int ligt_intensity;
  ligt_intensity = analogRead(LIGHT_PIN);
  //从传感器读取数据到串口
  int flameSensor = analogRead(FLAME_PIN);
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
      digitalWrite(HEAT_PIN, HIGH);
      Serial.print("heat\n");
    }
    else
    {
      digitalWrite(HEAT_PIN, LOW);
    }
    if (open[1])
    {
      //TODO:开启加湿装置
      digitalWrite(HUMI_PIN, HIGH);
      Serial.print("humi\n");
    }
    else
    {
      digitalWrite(HUMI_PIN, LOW);
    }
    if (open[2])
    {
      //TODO:开启加光装置
      digitalWrite(LIGHT_PIN, HIGH);
      Serial.print("light\n");
    }
    else
    {
      digitalWrite(LIGHT_PIN, LOW);
    }
    if (open[3])
    {
      //TODO:开启加压装置
      digitalWrite(PRESS_PIN, HIGH);
      Serial.print("press\n");
    }
    else
    {
      digitalWrite(PRESS_PIN, LOW);
    }
    readCompleted = false;
  }
  delay(1000);
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
