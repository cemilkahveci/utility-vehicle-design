{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87aaecbe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- Vehicle Performance Analysis ---\n",
      "Engine Torque: 13.85 Nm\n",
      "Wheel Torque (after 20:1 reduction): 235.39 Nm\n",
      "Tractive Effort: 941.54 N\n",
      "Max Theoretical Total Mass on 10.0% slope: 964.57 kg\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "def calculate_slope_performance():\n",
    "    # --- Input Parameters ---\n",
    "    power_hp = 7.0           # Motor gücü (HP)\n",
    "    rpm = 3600               # Motor devri (d/dak)\n",
    "    reduction_ratio = 20.0   # Toplam redüksiyon oranı (20:1)\n",
    "    wheel_radius_m = 0.20    #meter\n",
    "    slope_percent = 10.0     \n",
    "    efficiency = 0.8        # transmission eff.\n",
    "    \n",
    "    # --- Constants ---\n",
    "    hp_to_watts = 745.7\n",
    "    g = 9.81\n",
    "    \n",
    "    # 1. Motor Torku (Nm)\n",
    "    # Power (W) = Torque (Nm) * Angular Velocity (rad/s)\n",
    "    power_watts = power_hp * hp_to_watts\n",
    "    angular_velocity = (2 * math.pi * rpm) / 60\n",
    "    engine_torque = power_watts / angular_velocity\n",
    "    \n",
    "    # 2. Tekerlekteki Toplam Tork (Nm)\n",
    "    wheel_torque = engine_torque * reduction_ratio * efficiency\n",
    "    \n",
    "    # 3. Tekerlekteki Çekiş Kuvveti (N)\n",
    "    tractive_effort = wheel_torque / wheel_radius_m\n",
    "    \n",
    "    # 4. Eğim Açısı (Radyan)\n",
    "    slope_angle_rad = math.atan(slope_percent / 100)\n",
    "    \n",
    "    # 5. Maksimum Toplam Kütle (kg)\n",
    "    # F = m * g * sin(theta) -> Sadece eğim direncini yenecek kütle\n",
    "    max_total_mass = tractive_effort / (g * math.sin(slope_angle_rad))\n",
    "    \n",
    "    print(f\"--- Vehicle Performance Analysis ---\")\n",
    "    print(f\"Engine Torque: {engine_torque:.2f} Nm\")\n",
    "    print(f\"Wheel Torque (after 20:1 reduction): {wheel_torque:.2f} Nm\")\n",
    "    print(f\"Tractive Effort: {tractive_effort:.2f} N\")\n",
    "    print(f\"Max Theoretical Total Mass on {slope_percent}% slope: {max_total_mass:.2f} kg\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    calculate_slope_performance()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "traffic",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
