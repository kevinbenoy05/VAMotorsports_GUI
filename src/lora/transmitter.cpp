/*License: CC 4.0 - Attribution, NonCommercial (by Mitch Davis, github.com/thekakester)
* https://creativecommons.org/licenses/by-nc/4.0/   (See README for details)*/
#include <LoraSx1262.h>
byte payload[255];
LoraSx1262 radio;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Booted");

  if (!radio.begin()) { //Initialize radio
    Serial.println("Failed to initialize radio.");
  }
}
void loop() {
  Serial.print("Transmitting... ");
  radio.transmit(payload, 255);
  Serial.println("Done!");
  delay(1000);
}