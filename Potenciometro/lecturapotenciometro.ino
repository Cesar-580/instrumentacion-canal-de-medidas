void setup() {
  Serial.begin(9600);
}

void loop() {
  double valorleido = analogRead(A0); //potentiometer reading
  double longitud = valorleido * 5 * 2.06 / 1023; //Valor en cm
  Serial.print(longitud);
  delay(500);
}
