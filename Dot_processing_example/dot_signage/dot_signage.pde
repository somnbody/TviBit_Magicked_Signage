OPC opc;
PImage dot;

void setup()
{
  size(800, 200);

  // Load a sample image
  dot = loadImage("color-dot.png");

  // Connect to the local instance of fcserver
  opc = new OPC(this, "10.80.31.24", 7890);

  // Map one 64-LED strip to the center of the window
  opc.ledStrip(0, 15, width+100, height-200, width / 70.0, 0, false);
  opc.ledStrip(15, 15, width+98, height-195, width / 70.0, 0, true);
  opc.ledStrip(30, 15, width+96, height-190, width / 70.0, 0, false);
  opc.ledStrip(45, 15, width+94, height-185, width / 70.0, 0, true);
  opc.ledStrip(60, 15, width+92, height-180, width / 70.0, 0, false);
  //bottom angled part of T in TviBit
  opc.ledStrip(75, 15, width+100, height/2, width / 70.0, 250, true);
  opc.ledStrip(90, 15, width+95, height/2, width / 70.0, 250, false);
  opc.ledStrip(105, 15, width+90, height/2, width / 70.0, 250, true);
  opc.ledStrip(120, 15, width+85, height/2, width / 70.0, 250, false);
  opc.ledStrip(135, 15, width+80, height/2, width / 70.0, 250, true);
}

void draw()
{
  background(0);

  // Draw the image, centered at the mouse location
  float dotSize = width * 0.2;
  image(dot, mouseX - dotSize, mouseY - dotSize/2, dotSize, dotSize);
}
