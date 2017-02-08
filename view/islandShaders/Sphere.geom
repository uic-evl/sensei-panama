#version 150 compatibility
#extension GL_EXT_geometry_shader4: enable
#extension GL_ARB_gpu_shader5 : enable

uniform float pointScale;

flat out vec3 vertex_light_position;
flat out vec4 eye_position;
flat out float sphere_radius;

uniform float globalAlpha;
uniform int toggleTrees;

void
main(void)
{
	sphere_radius =  pointScale * 2.0;
	float halfsize = sphere_radius * 0.5;
    gl_FrontColor = gl_FrontColorIn[0];
    if (toggleTrees == 1) {
	   gl_FrontColor.a = globalAlpha;
    }
    else {
        if (((gl_FrontColor.r*255 - gl_FrontColor.g*255) > 7) && 
           (gl_FrontColor.r*255 > 37) && (gl_FrontColor.r*255 < 160) &&
           ((gl_FrontColor.b*255 - gl_FrontColor.g*255) > 1) &&
           (gl_FrontColor.b*255 > 36) && (gl_FrontColor.b*255 < 140)) {

            gl_FrontColor.a = 1.0;
        }
        else {
            gl_FrontColor.a = 0.1;
        }
    }


	//Example using the gl_FrontColor values for filtering!!
	//now these hold colors.  in our case they will store r=day, g=hr, b=min, a=individualId
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
