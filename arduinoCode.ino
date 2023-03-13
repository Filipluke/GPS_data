#include <TinyGPS++.h>
#include <SoftwareSerial.h>

static const int RXPin = 4, TXPin = 3;
static const uint32_t GPSBaud = 9600;

TinyGPSPlus gps;

SoftwareSerial ss(RXPin, TXPin);

void setup()
{
  Serial.begin(9600);
  ss.begin(GPSBaud);

 
}

void loop()
{
  while (ss.available() > 0)
    if (gps.encode(ss.read()))
      displayInfo();

  if (millis() > 5000 && gps.charsProcessed() < 10)
  {
    Serial.println(F("No GPS detected: check wiring."));
    while(true);
  }
}

void displayInfo()
{
  //Serial.print(F("Location: ")); 
  if (gps.location.isValid())
  {
   // Serial.print(gps.location.lat(), 6);
   //  Serial.print(F(", "));
   // Serial.print(gps.location.lng(), 6);
   // Serial.print(F(", "));
   // Serial.print(millis());
   //  Serial.print(F(", "));
  }
  else
  {
    Serial.print(F("INVALID "));
    //diode light on/off
  }

  //Serial.print(F("  Date "));
  if (gps.date.isValid())
  {
    /*Serial.print(F("/"));
    Serial.print(gps.date.day());
    Serial.print(F("/"));
    Serial.print(gps.date.month());
    Serial.print(gps.date.year());
    Serial.print(F("  Velocity "));*/
    Serial.println(gps.speed.kmph());
    //Serial.println(" Satellite Count: ");
    //Serial.println(gps.satellites.value());
  }
  else
  {
    Serial.print(F("INVALID "));
    
  }

  
  Serial.println();
}