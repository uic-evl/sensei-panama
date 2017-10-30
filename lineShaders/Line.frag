#version 150 compatibility
#extension GL_ARB_gpu_shader5 : enable

void main(void)
{
    if (gl_Color[3] >= 0.98)
        gl_FragColor = gl_Color;
    else
        gl_FragColor = vec4(0, 0, 0, 0);
}