import arcade
arcade.open_window(800,800, "My Beautiful Home")
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(200, 600, 600, 200, arcade.color.BITTER_LEMON)
arcade.draw_lrtb_rectangle_filled(350, 450, 350, 200, arcade.color.BISTRE_BROWN )
arcade.draw_lrtb_rectangle_outline(250, 350, 525, 400, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_outline(450, 550, 525, 400, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.GREEN)
arcade.draw_triangle_filled(150, 600, 400, 750, 650, 600, arcade.color.AMARANTH_PURPLE)
arcade.draw_circle_filled(425, 275, 10, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(425, 500, 775, 600, arcade.color.BRICK_RED)
arcade.draw_circle_filled(100, 700, 75, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(75, 700, 25, arcade.color.WHITE_SMOKE)
arcade.finish_render()
arcade.run()