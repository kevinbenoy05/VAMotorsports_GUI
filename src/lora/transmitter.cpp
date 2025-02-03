/*License: CC 4.0 - Attribution, NonCommercial (by Mitch Davis, github.com/thekakester)
* https://creativecommons.org/licenses/by-nc/4.0/   (See README for details)*/
#include <LoraSx1262.h>
byte payload = "Hello World!";
LoraSx1262* radio;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Booted");

  // if (!radio.begin()) { //Initialize radio
  //   Serial.println("Failed to initialize radio.");
  // }
  radio = new LoraSx1262();

  // data in payload
  // for (int i = 0; i < 255; i++) {
  //   payload[i] = i;
  // }
}
void loop() {
  const char *message = "Hello World!";
  Serial.print("Transmitting... ");
  radio->transmit(payload, strlen(payload));
  Serial.println("Done!");
  delay(1000);
}