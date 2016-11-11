#version 150 compatibility
#extension GL_EXT_geometry_shader4: enable
#extension GL_ARB_gpu_shader5 : enable

uniform float movePointScale;

<<<<<<< HEAD
uniform int startDay;                       //start date of gps tracking info
uniform int endDay;                         //end date of gps tracking info

uniform int colorBy;                        //maps what color is used
uniform int selectedIndividual1;            //drawing individual 1
uniform int selectedIndividual2;            //drawing individual 2
=======
uniform int startDay[21];
uniform int endDay[21];

uniform int bitMapSelectedIndividuals[21];
uniform int colorByBitMap[21];
>>>>>>> master


flat out vec3 vertex_light_position;
flat out vec4 eye_position;
flat out float sphere_radius;

void
main(void)
{
  sphere_radius =  movePointScale * 2.0;
  float halfsize = sphere_radius * 0.5;

  gl_FrontColor = gl_FrontColorIn[0];
  //gl_FrontColor.a = globalAlpha;

	highp int day = int(gl_FrontColor.r);
	highp int hr = int(gl_FrontColor.g);
	highp int minute = int(gl_FrontColor.b);
  highp int individualID = int(gl_FrontColor.a);
  float dayModSeven = mod(day, 7);
  int saveIndInfo;

  const int selectedIndividuals[21] = int[21](4690, 4693, 4652, 4653, 4658, 4052, 4672, 4668, 4671, 4669, 4675, 4650, 4674, 4689, 4654, 4657, 4660, 4692, 4673, 4656, 4665);
	  
	//Example using the gl_FrontColor values for filtering!!
<<<<<<< HEAD
	bool drawPoint = true;

  //figure out if this point will be drawn
  //day = 1, startDay =1 endDay =2 -> draw
  //day = 2 or 0, startDay = 1 end day = 2 not draw
  //if( individualID - 4693 == 0)//selectedIndividual1 || individualID == selectedIndividual2 )
  //    drawPoint = true; 
  if( drawPoint && (day >= startDay && day < endDay) )
	    drawPoint = true;
  else
      drawPoint = false;
=======
	bool drawPoint = false;

  if((day >= startDay[0]) && (day < endDay[0]) && (bitMapSelectedIndividuals[0] == 1) && (selectedIndividuals[0] == individualID)) 
  {
    saveIndInfo = 0;
    drawPoint = true;
  }
  if((day >= startDay[1]) && (day < endDay[1]) && (bitMapSelectedIndividuals[1] == 1) && (selectedIndividuals[1] == individualID)) 
  {
    saveIndInfo = 1;
    drawPoint = true;
  }
  if((day >= startDay[2]) && (day < endDay[2]) && (bitMapSelectedIndividuals[2] == 1) && (selectedIndividuals[2] == individualID)) 
  {
    saveIndInfo = 2;
    drawPoint = true;
  }
  if((day >= startDay[3]) && (day < endDay[3]) && (bitMapSelectedIndividuals[3] == 1) && (selectedIndividuals[3] == individualID)) 
  {
    saveIndInfo = 3;
    drawPoint = true;
  }
  if((day >= startDay[4]) && (day < endDay[4]) && (bitMapSelectedIndividuals[4] == 1) && (selectedIndividuals[4] == individualID)) 
  {
    saveIndInfo = 4;
    drawPoint = true;
  }
  if((day >= startDay[5]) && (day < endDay[5]) && (bitMapSelectedIndividuals[5] == 1) && (selectedIndividuals[5] == individualID)) 
  {
    saveIndInfo = 5;
    drawPoint = true;
  }
  if((day >= startDay[6]) && (day < endDay[6]) && (bitMapSelectedIndividuals[6] == 1) && (selectedIndividuals[6] == individualID)) 
  {
    saveIndInfo = 6;
    drawPoint = true;
  }
  if((day >= startDay[7]) && (day < endDay[7]) && (bitMapSelectedIndividuals[7] == 1) && (selectedIndividuals[7] == individualID)) 
  {
    saveIndInfo = 7;
    drawPoint = true;
  }
  if((day >= startDay[8]) && (day < endDay[8]) && (bitMapSelectedIndividuals[8] == 1) && (selectedIndividuals[8] == individualID)) 
  {
    saveIndInfo = 8;
    drawPoint = true;
  }
  if((day >= startDay[9]) && (day < endDay[9]) && (bitMapSelectedIndividuals[9] == 1) && (selectedIndividuals[9] == individualID)) 
  {
    saveIndInfo = 9;
    drawPoint = true;
  }
  if((day >= startDay[10]) && (day < endDay[10]) && (bitMapSelectedIndividuals[10] == 1) && (selectedIndividuals[10] == individualID)) 
  {
    saveIndInfo = 10;
    drawPoint = true;
  }
  if((day >= startDay[11]) && (day < endDay[11]) && (bitMapSelectedIndividuals[11] == 1) && (selectedIndividuals[11] == individualID)) 
  {
    saveIndInfo = 11;
    drawPoint = true;
  }
  if((day >= startDay[12]) && (day < endDay[12]) && (bitMapSelectedIndividuals[12] == 1) && (selectedIndividuals[12] == individualID)) 
  {
    saveIndInfo = 12;
    drawPoint = true;
  }
  if((day >= startDay[13]) && (day < endDay[13]) && (bitMapSelectedIndividuals[13] == 1) && (selectedIndividuals[13] == individualID)) 
  {
    saveIndInfo = 13;
    drawPoint = true;
  }
  if((day >= startDay[14]) && (day < endDay[14]) && (bitMapSelectedIndividuals[14] == 1) && (selectedIndividuals[14] == individualID)) 
  {
    saveIndInfo = 14;
    drawPoint = true;
  }
  if((day >= startDay[15]) && (day < endDay[15]) && (bitMapSelectedIndividuals[15] == 1) && (selectedIndividuals[15] == individualID)) 
  {
    saveIndInfo = 15;
    drawPoint = true;
  }
  if((day >= startDay[16]) && (day < endDay[16]) && (bitMapSelectedIndividuals[16] == 1) && (selectedIndividuals[16] == individualID)) 
  {
    saveIndInfo = 16;
    drawPoint = true;
  }
  if((day >= startDay[17]) && (day < endDay[17]) && (bitMapSelectedIndividuals[17] == 1) && (selectedIndividuals[17] == individualID)) 
  {
    saveIndInfo = 17;
    drawPoint = true;
  }
  if((day >= startDay[18]) && (day < endDay[18]) && (bitMapSelectedIndividuals[18] == 1) && (selectedIndividuals[18] == individualID)) 
  {
    saveIndInfo = 18;
    drawPoint = true;
  }
  if((day >= startDay[19]) && (day < endDay[19]) && (bitMapSelectedIndividuals[19] == 1) && (selectedIndividuals[19] == individualID)) 
  {
    saveIndInfo = 19;
    drawPoint = true;
  }
  if((day >= startDay[20]) && (day < endDay[20]) && (bitMapSelectedIndividuals[20] == 1) && (selectedIndividuals[20] == individualID)) 
  {
    saveIndInfo = 20;
    drawPoint = true;
  }


  //gl_FrontColor.a = globalAlpha;

  //***********************************************************************************************
  //Don't worry about this. It's computing a color by time
>>>>>>> master
	    
	if( drawPoint ) {

    gl_FrontColor = vec4( 255.0/255.0, 0.0, 0.0, 1.0); 

    if( colorByBitMap[saveIndInfo] == 0 ){ //one color palette
      if( hr < 4 )
        gl_FrontColor = vec4( 255.0/255.0,255.0/255.0,204.0/255.0, 1.0 );
      if( hr >= 4 && hr < 8 )
        gl_FrontColor = vec4( 199.0/255.0,233.0/255.0,180.0/255.0, 1.0 );
      if( hr >= 8 && hr < 12 )
        gl_FrontColor = vec4(127.0/255.0,205.0/255.0,187.0/255.0, 1.0 );
      if( hr >= 12 && hr < 16 )
        gl_FrontColor = vec4( 65.0/255.0,182.0/255.0,196.0/255.0, 1.0 );
      if( hr >= 16 && hr < 20 )
        gl_FrontColor = vec4( 44.0/255.0,127.0/255.0,184.0/255.0, 1.0 );
      if( hr >= 20 && hr < 24 )
        gl_FrontColor = vec4( 37.0/255.0,52.0/255.0,148.0/255.0, 1.0 );
    }
    if( colorByBitMap[saveIndInfo] == 1 ){
      if( hr < 3 )
        gl_FrontColor = vec4( 69.0/255.0,117.0/255.0,180.0/255.0, 1.0 );
      if( hr >= 3 && hr < 6 )
        gl_FrontColor = vec4( 116.0/255.0,173.0/255.0,209.0/255.0, 1.0 );
      if( hr >= 6 && hr < 9 )
        gl_FrontColor = vec4(171.0/255.0,217.0/255.0,233.0/255.0, 1.0 );
      if( hr >= 9 && hr < 12 )
        gl_FrontColor = vec4( 224.0/255.0,243.0/255.0,248.0/255.0, 1.0 );
      if( hr >= 12 && hr < 15 )
        gl_FrontColor = vec4( 254.0/255.0,224.0/255.0,144.0/255.0, 1.0 );
      if( hr >= 15 && hr < 18 )
        gl_FrontColor = vec4( 253.0/255.0,174.0/255.0,97.0/255.0, 1.0 );
      if( hr >= 18 && hr < 21 )
        gl_FrontColor = vec4( 244.0/255.0,109.0/255.0,67.0/255.0, 1.0 );
      if( hr >= 21 && hr < 24 )
        gl_FrontColor = vec4( 215.0/255.0,48.0/255.0,39.0/255.0, 1.0 );
    }
    if( colorByBitMap[saveIndInfo] == 2){
      if( hr < 3 )
        gl_FrontColor = vec4( 104.0/255.0,79.0/255.0,227.0/255.0, 1.0 );
      if( hr >= 3 && hr < 6 )
        gl_FrontColor = vec4( 78.0/255.0,181.0/255.0,226.0/255.0, 1.0 );
      if( hr >= 6 && hr < 9 )
        gl_FrontColor = vec4( 138.0/255.0,227.0/255.0,244.0/255.0, 1.0 );
      if( hr >= 9 && hr < 12 )
        gl_FrontColor = vec4( 253.0/255.0,247.0/255.0,155.0/255.0, 1.0 );
      if( hr >= 12 && hr < 15 )
        gl_FrontColor = vec4( 253.0/255.0,222.0/255.0,115.0/255.0, 1.0 );
      if( hr >= 15 && hr < 18 )
        gl_FrontColor = vec4( 253.0/255.0,247.0/255.0,155.0/255.0, 1.0 );
      if( hr >= 18 && hr < 21 )
        gl_FrontColor = vec4( 138.0/255.0,227.0/255.0,244.0/255.0, 1.0 );
      if( hr >= 21 && hr < 24 )
        gl_FrontColor = vec4( 78.0/255.0,181.0/255.0,226.0/255.0, 1.0 );
    }
    if( colorByBitMap[saveIndInfo] == 3){
      if( dayModSeven == 0 )
        gl_FrontColor = vec4( 247.0/255.0,251.0/255.0,255.0/255.0, 1.0 );
      if( dayModSeven == 1 )
        gl_FrontColor = vec4( 222.0/255.0,235.0/255.0,247.0/255.0, 1.0 );
      if( dayModSeven == 2 )
        gl_FrontColor = vec4( 198.0/255.0,219.0/255.0,239.0/255.0, 1.0 );
      if( dayModSeven == 3 )
        gl_FrontColor = vec4( 158.0/255.0,202.0/255.0,225.0/255.0, 1.0 );
      if( dayModSeven == 4 )
        gl_FrontColor = vec4( 107.0/255.0,174.0/255.0,214.0/255.0, 1.0 );
      if( dayModSeven == 5 )
        gl_FrontColor = vec4( 66.0/255.0,146.0/255.0,198.0/255.0, 1.0 );
      if( dayModSeven == 6 )
        gl_FrontColor = vec4( 33.0/255.0,113.0/255.0,181.0/255.0, 1.0 );
      //if( day >= 70 && day < 84 )
      //  gl_FrontColor = vec4( 8.0/255.0,81.0/255.0,156.0/255.0, 1.0 );
    }
    if( colorByBitMap[saveIndInfo] == 4){
      if( day < 10 )
        gl_FrontColor = vec4( 255.0/255.0,247.0/255.0,243.0/255.0, 1.0 );
      if( day >= 10 && day < 20 )
        gl_FrontColor = vec4( 253.0/255.0,224.0/255.0,221.0/255.0, 1.0 );
      if( day >= 20 && day < 30 )
        gl_FrontColor = vec4( 252.0/255.0,197.0/255.0,192.0/255.0, 1.0 );
      if( day >= 30 && day < 40 )
        gl_FrontColor = vec4( 250.0/255.0,159.0/255.0,181.0/255.0, 1.0 );
      if( day >= 40 && day < 50 )
        gl_FrontColor = vec4( 247.0/255.0,104.0/255.0,161.0/255.0, 1.0 );
      if( day >= 50 && day < 60 )
        gl_FrontColor = vec4( 221.0/255.0,52.0/255.0,151.0/255.0, 1.0 );
      if( day >= 60 && day < 70 )
        gl_FrontColor = vec4( 174.0/255.0,1.0/255.0,126.0/255.0, 1.0 );
      if( day >= 70 && day < 84 )
        gl_FrontColor = vec4( 122.0/255.0,1.0/255.0,119.0/255.0, 1.0 );
    }
    if( colorByBitMap[saveIndInfo] == 5 ){
      if( bitMapSelectedIndividuals[saveIndInfo] == 1 )
        if (mod(individualID, 3) == 0)
          gl_FrontColor = vec4( mod(individualID, 255.0),79.0/255.0,234.0/255.0, 1.0 );
        if (mod(individualID, 3) == 1)
          gl_FrontColor = vec4( 149.0/255.0,mod(individualID, 255.0),234.0/255.0, 1.0 );
        if (mod(individualID, 3) == 2)
          gl_FrontColor = vec4( 149.0/255.0,79.0/255.0,mod(individualID, 255.0), 1.0 );
    }


    //**********************************************************************************************
    //Here is our changes to the .geom

    eye_position = gl_PositionIn[0];
    vertex_light_position = normalize(gl_LightSource[0].position.xyz - eye_position.xyz);

    gl_TexCoord[0].st = vec2(1.0,-1.0);
    gl_Position = gl_PositionIn[0];
    gl_Position.xy += vec2(halfsize, -halfsize);
    gl_Position = gl_ProjectionMatrix * gl_Position;
    EmitVertex();
      
    gl_TexCoord[0].st = vec2(1.0,1.0);
    gl_Position = gl_PositionIn[0];
    gl_Position.xy += vec2(halfsize, halfsize);
    gl_Position = gl_ProjectionMatrix * gl_Position;
    EmitVertex();

    gl_TexCoord[0].st = vec2(-1.0,-1.0);
    gl_Position = gl_PositionIn[0];
    gl_Position.xy += vec2(-halfsize, -halfsize);
    gl_Position = gl_ProjectionMatrix * gl_Position;
    EmitVertex();

    gl_TexCoord[0].st = vec2(-1.0,1.0);
    gl_Position = gl_PositionIn[0];
    gl_Position.xy += vec2(-halfsize, halfsize);
    gl_Position = gl_ProjectionMatrix * gl_Position;
    EmitVertex();
      
    EndPrimitive();
	}
}
