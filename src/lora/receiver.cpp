/*License: CC 4.0 - Attribution, NonCommercial (by Mitch Davis, github.com/thekakester)
* https://creativecommons.org/licenses/by-nc/4.0/   (See README for details)*/
#include <LoraSx1262.h>
LoraSx1262 receiver;
byte receiveBuff[255];
void setup() {
  Serial.begin(9600);
  Serial.println("Booted");

  if (!receiver.begin()) { //Initialize the radio
    Serial.println("Failed to initialize radio");
  }
}
void loop() {
  //Receive a packet over radio
  int bytesRead = receiver.lora_receive_async(receiveBuff, sizeof(receiveBuff));
  if (bytesRead > -1) {
    Serial.write(receiveBuff, bytesRead);
    Serial.println();
  }
}