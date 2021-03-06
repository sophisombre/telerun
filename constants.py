# Все используемые константы (то, что никак не меняется где бы то ни было)
win_w = 800  # Ширина окна
win_h = int(3 * win_w / 4)  # Высота окна
scaling = win_w / 800  # Масштаб (все константы лучше задавать через него. Например: spd = 7 * scaling)

# Константы, необходимые для отрисовки самолётика
pl_w = 120 * scaling  # Ширина фигуры самолётика
pl_h = pl_w / 3  # Высота фигуры самолётика

midle_x = (win_w - pl_w) / 2  # Координаты самолётика, при которых он отобр. в центре экрана
midle_y = (win_h - pl_h) / 2
pl_x0 = midle_x  # Стартовыеоординаты самолётика
pl_y0 = midle_y

spd = 7  # Скорость самолетика вдоль оси OX
pl_g = 0.6  # Ускорение свободного самолёта
a_down = pl_g * 1.2  # Ускорение самолета при движении вниз
shell_r = 3  # Радиус снаряда
delay = 20

# Необходимо ограничить движение самолётика вдоль оси Х
brd = spd  # min расстояние на которое самолетик может приблизится к краям экрана

# Константы, необходимые для отрисовки облаков
cld_w = int(196 * scaling)
cld_h = int(127 * scaling)
shift = int(0.3 * cld_h)

cld_v = 4 * scaling  # Скорость движения облаков, с ней можно играться
