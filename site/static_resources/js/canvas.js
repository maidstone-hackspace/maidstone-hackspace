document.onkeypress = function(e){
        e = e || window.event;
        kcode = e.keyCode || e.which;
        if (kcode == 32 && jump_height==0){ //space bar
            jump_force = 8;
            score.innerHTML = parseInt(score.innerHTML) + 1;
        }
        console.log(kcode);
        // do something with key
};


var canvas = document.getElementById("scene");
var score = document.getElementById("score");

var ctx = canvas.getContext("2d");
var canvas_width = canvas.width; //800;
var canvas_height = canvas.height; //800;
//~ var y = canvas_height / 2; // # middle of the screen
var canvas_center_x = canvas_width / 2; // # middle of the screen
var canvas_center_y = canvas_height / 2; // # middle of the screen

var grd=ctx.createLinearGradient(0, canvas_center_y, 0, canvas_height);
        
ctx.lineWidth = 10;
ctx.strokeStyle = '#ff0000';

// wave settings
var wave_points = 10;
var sample_rate = canvas_width;  // sample rate
var frequency = 6.0; // The frequency of a sine wave is the number of complete cycles that happen every second. 
var amplitude = 30.0; // how many pixels tall the waves with rise/fall.
var velocity = parseFloat(canvas_width); //
var wavelength = velocity / frequency; //λ

var timeloop_multiplier = 1;

window.addEventListener('resize', resizeCanvas, false);

function resizeCanvas(){
    canvas.width = window.innerWidth;
    //~ canvas.height = window.innerHeight;
    canvas_width = canvas.width; //800;
    canvas_height = canvas.height; //800;
    y = canvas_height / 2; // # middle of the screen
    canvas_center_x = canvas_width / 2; // # middle of the screen
    canvas_center_y = canvas_height / 2; // # middle of the screen
    
    // Calculate gradient in relation to the screen size
    grd = ctx.createLinearGradient(0, canvas_center_y, 0, canvas_height);
    grd.addColorStop(0, "#0087A8");
    grd.addColorStop(1, "#0087A8");
    ctx.fillStyle = grd;
}
resizeCanvas();

var t = 0;

var pi2 = Math.PI * 2.0;
var pi2_frequency = pi2 * frequency;

function timeloop(wavelength, multiplyer){
    /* looped time, instead of continuosly counting up 
    # we just repeat once one wavelength has been travelled*/
    var a = 0;
    wavelength_max = Math.ceil(wavelength / multiplyer);
    while (true){
        if (a > wavelength_max)
            a = 0;
        //~ yield a;
        a += multiplyer;
    }
}
function timeloop_new(t, wavelength, multiplyer){
    /* looped time, instead of continuosly counting up 
       we just repeat once one wavelength has been travelled */
    wavelength_max = Math.ceil(wavelength / multiplyer) * multiplyer;
    t += multiplyer;
    // 0 and wavelength are the same, so start on multiplyer ie first step
    if (t > wavelength_max)
        t = multiplyer;
    return t;
}

function wave_point(time, x, y, amplitude, frequency, sample_rate){
    cr = Math.cos((pi2_frequency * ((x + time) / sample_rate)))
    new_y = y + amplitude * cr;
    return [x, new_y, cr];
}

// calculate vector between two points and normalise the result
function vector_norm(p1, p2){
    a1 = p2[0] - p1[0];
    a2 = p2[1] - p1[1];
    length = Math.sqrt((a1 * a1) + (a2 * a2));
    return  [a1 / length, a2 / length];
}

function draw_triangle(p1, p2, p3){
    
}

// calculate the dot product of two vectors then pass the dot to 
// acos to get a angle in radians
function triangle_angle(p1, p2, p3){
    a = vector_norm(p1, p2); // vector 1
    b = vector_norm(p1, p3);
    dot = a[0] * b[0] + a[1] * b[1];
    return Math.acos(dot);
}

function calculate_image_angle(p1, p2){
    // Draw the duck, calculate the angle by creating a right angled traingle from the wave points 
    if(p1[1] > p2[1]){
        angle = -triangle_angle(
            [p1[0] - 10, p1[1]], 
            p2, 
            p1);
    }else{
        angle = triangle_angle(
            [p1[0] - 10, p1[1]], 
            p2, 
            p1);
    }
    return angle;
}


function draw_character(point, angle){
    // Draw the duck
    ctx.save();
    ctx.translate(point[0], point[1] - 16);
    ctx.rotate(angle);
    ctx.drawImage(img, -16, -16, 32, 32);
    ctx.restore();
}


function draw_wave(){
    // Draw the wave polygon
    ctx.beginPath(); 
    ctx.moveTo(0, canvas_height);
    for (p=0;p < points.length; p=p+1){
        ctx.lineTo(parseInt(points[p][0]), parseInt(points[p][1]));
    }
    ctx.lineTo(canvas_width, canvas_height);
    ctx.lineWidth = 10;
    ctx.stroke();
    ctx.fill();
}

function draw_wave_points(){
    // Draw the wave points, usefull for debuging
    ctx.beginPath(); 
    //~ ctx.moveTo(-10, canvas_height);
    for (p=0;p < points.length; p=p+1){
        ctx.arc(parseInt(points[p][0]), parseInt(points[p][1]),2,0,2*Math.PI);
    }
    ctx.stroke();
}

// Calculate the initial wave polygon, at time 0 then step to the next time index
var points = new Array();
var point = null;
for (x_pos = 0; x_pos < canvas_width + 1; x_pos = x_pos + 10) {
    for (p=0;p < points.length; p = p + 1){
        points[p][0] = points[p][0] - wave_points;
    }
    point = wave_point(time=t, x=canvas_width, y=canvas_center_y, amplitude=amplitude, frequency=frequency, sample_rate=sample_rate);
    points.push([point[0], point[1]]);
    t = timeloop_new(t, wavelength, timeloop_multiplier);
}



var angle = null;
var center_point = Math.ceil(points.length / 2);
var img = new Image();
img.src = '/static/images/icon.png';

var rotate = 0;

var world_gravity = 0.75;
var jump_height = 0;
var jump_force = 0;


function drawScene(){
    ctx.clearRect(0, 0, canvas_width, canvas_height);

    // shift each points along by wave point distance, remove the first item on the array
    // push a new point to the end of the wave
    for (p=0;p < points.length; p = p + 1){
        points[p][0] = points[p][0] - wave_points;
    }
    points.shift();
    points.push(wave_point(time=t, x=canvas_width, y=canvas_center_y, amplitude=amplitude, frequency=frequency, sample_rate=sample_rate));

    if (jump_height > 0 || jump_force > 0){
        jump_height += jump_force;
        jump_force -= world_gravity;
    }else{
        jump_force = 0;
        jump_height = 0;
    }

    //angle = calculate_image_angle(points[center_point - 1], points[center_point]);
    rotate = rotate + 0.1;
    draw_character(
        [points[center_point][0], points[center_point][1] - jump_height], 
        rotate
    );
    //~ draw_character(
        //~ points[center_point - 8], 
        //~ rotate
    //~ );
    //~ draw_character(
        //~ points[center_point - 16], 
        //~ rotate
    //~ );

    draw_wave();
    //~ draw_wave_points();

    t = timeloop_new(t, wavelength, timeloop_multiplier);
    requestAnimationFrame(drawScene);
}

drawScene();
