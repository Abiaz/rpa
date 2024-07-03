# -*- coding: utf-8 -*-
"""
RPA Workflow / main application

@author: python-rpa-dev

Date        Author          Info
-------------------------------------------------------------------------------
2022.06.20  python-rpa-dev  Initial Version
2022.06.29  python-rpa-dev  Set loglevel with environment variable RPA_LOGLEVEL
                            see https://powerfulpython.com/blog/nifty-python-logging-trick/2022.06.29  python-rpa-dev  Add checksum so we can use versioning for data collection etc.

"""

import logging
from pyrpa.lib_config import load_config
from pyrpa.lib_rpa import Robotic_Process_Automation
from pyrpa.lib_secv import gen_checksum
import os
import argparse


logger = logging.getLogger(__name__)

def auto():

    rpa.wait_and_click(['btn_asgard_guild_raid_sk1.png','btn_asgard_guild_raid_sk2.png','btn_asgard_guild_raid_sk3.png','btn_asgard_guild_raid_start.png','btn_asgard_guild_raid_next.png', 'btn_asgard_guild_raid_battle.png', 'btn_asgard_guild_raid_next2.png', 'btn_asgard_guild_raid_battle2.png','btn_asgard_guild_raid_auto.png','btn_asgard_guild_raid_skip.png','btn_asgard_guild_raid_ok.png'])


def heroic_mission():

    rpa.wait_and_click (['btn_heroic_mission_campaign3.png','btn_heroic_mission_campaign3.png','btn_heroic_mission_kampagne.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_heroic_mission_left.png','btn_heroic_mission_left2.png','btn_heroic_mission_left3.png'], confidence=0.7)

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_heroic_mission_aurora.png'], max_wait=3)
            rpa.wait_and_click(['btn_heroic_mission_mouse.png'], max_wait=3)
                           
            rpa.restore_queue('start_loop')

    rpa.wait_and_click (['btn_heroic_mission_x3.png'], confidence=0.9)

    rpa.press('esc', presses=5, interval= 0.5)

    

def spooky():

    rpa.press('esc', presses=5, interval= 0.5)

    rpa.wait_and_click (['btn_spooky_pumpkin.png'])

    
    if rpa.end_of_queue_state():
        rpa.wait_and_click (['btn_spooky_furnace.png'])

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
            rpa.wait_and_click (['btn_spooky_enter.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click (['btn_spooky_130.png'])

                if rpa.end_of_queue_state():
                    rpa.wait_and_click(['btn_spooky_albus.png'], max_wait=5)
                    rpa.wait_and_click(['btn_spooky_pet.png'])

                    if rpa.end_of_queue_state():
                        rpa.wait_and_click(['btn_spooky_albus.png'])

                        if rpa.end_of_queue_state():
                            rpa.wait_and_click (['btn_spooky_battle.png'])

                            if rpa.end_of_queue_state():
                                rpa.wait_and_click (['btn_spooky_auto.png'])

                                if rpa.end_of_queue_state():
                                    rpa.press('esc')

                                    if rpa.end_of_queue_state():
                                        rpa.wait_and_click (['btn_spooky_skip.png'])

                                        if rpa.end_of_queue_state():
                                            rpa.wait_and_click (['btn_spooky_ok.png'])
                                                                                                             
        rpa.restore_queue('start_loop')

        rpa.press ('f5')

        rpa.sleep (20)

        rpa.press('esc', presses=5, interval= 0.5)

       
def open_game():

    import webbrowser
    url = 'https://www.hero-wars.com/?hl=en'
    webbrowser.open_new(url)
    rpa.sleep(15)
    rpa.press ('f11')
    rpa.wait_and_click(['btn_start_game.png'])
    rpa.wait_and_click(['btn_login_cookies4.png','btn_login_cookies.png','btn_login_cookies2.png','btn_login_cookies3.png'])

def close_window():

    rpa.close_window ()

def logout():

    rpa.sleep(15)

    rpa.wait_and_click(['btn_logout_cancel.png'])
    
    rpa.press ('esc', presses=10, interval=0.1)

    rpa.sleep (10)

    rpa.wait_and_click(['btn_logout_menu.png'], confidence=0.7)

    if rpa.end_of_queue_state():
        rpa.press ('tab', presses=21, interval= 0.1)

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_logout.png','btn_logout_logout2.png','btn_logout_abmelden.png'])

        rpa.sleep(10)
    

def login_abiaz():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_abiaz.png','btn_login_abiaz2.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

    rpa.sleep(25)
    rpa.wait_and_click(['btn_logout_cancel.png'])
    rpa.press('esc', presses=5, interval= 0.5)
    rpa.wait_and_click(['btn_server.png','btn_server2.png','btn_server3.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_server_change.png'], confidence=0.9)

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_server_40.png'], confidence=0.9)

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_server_select.png'], confidence=0.9)

    rpa.sleep(25)
    rpa.press('f5')
    rpa.sleep(25)

        
    

def login_sonne():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_sonne.png','btn_login_sonne2.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

def login_agr():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_agr.png','btn_login_agr2.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

    rpa.sleep(25)

def login_claudi():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_claudi.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

    rpa.sleep(25)

def login_jens():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_jens.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

    rpa.sleep(25)

def login_stivio():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_stivio.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

    rpa.sleep(25)

def login_hathor():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_hathor.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

    rpa.sleep(25)

def login_moonchild():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_moonchild.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

    rpa.sleep(25)

def login_marc():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_marc.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png'])

def login_floki():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_floki.png','btn_login_floki2.png'])

        if rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

    rpa.sleep(25)

def login_schwadi():

    rpa.wait_and_click(['btn_login_email.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_login_schwadi.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_login_play.png','btn_login_jetztspielen.png'])

    rpa.sleep(25)

def hwh():

    rpa.sleep(25)
    rpa.wait_and_click(['btn_hwh_doit.png'])
    rpa.sleep(5)
    rpa.press('esc', presses=5, interval= 0.5)
    rpa.wait_and_click(['btn_hwh_actions.png'], confidence=0.9)
    rpa.wait_and_click(['btn_hwh_minions.png'], confidence=0.9)
    rpa.wait_and_click(['btn_hwh_run.png'], confidence=0.9)
    rpa.sleep(15)
    rpa.wait_and_click(['btn_hwh_doall.png'], confidence=0.9)
    rpa.wait_and_click(['btn_hwh_go.png'], confidence=0.9)
    rpa.wait_and_click(['btn_hwh_ignore.png'])
    rpa.wait_and_click(['btn_hwh_ignore.png'])
    rpa.wait_and_click(['btn_hwh_no.png'])
    rpa.wait_and_click(['btn_hwh_ok.png'], max_wait=300)
    rpa.sleep(25)
    
    

def first_screen():
    """
    for the first scan we allow multiple tries to the
    loading of the initial screen
    imp_pos = find_scaled_image('logo_nexters.png', tries = 10, sleep = 2)
    logger.info('(X/Y) %s:%s (W/H) %s:%s', imp_pos[0].left, imp_pos[0].top, imp_pos[0].width, imp_pos[0].height)

    Step: find nexters logo to lookup browser window
    img_pos, scale = find_and_click('logo_nexters.png', tries = 10, sleep = 2)
    # logger.info('image position %s', img_pos)
    """
    rpa.wait_and_click(['logo_nexters.png','logo_nexters2.png'], max_wait=20)  # check for loading screen and ads
    rpa.sleep(20)
    rpa.press('esc', presses=5, interval= 0.5)  # exit promotion screen

def server_40():
    """
    ----------------------------------------------------------------------
    Step: Change to Server 40
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_server.png','btn_server2.png','btn_server3.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_server_change.png'], confidence=0.9)

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_server_down.png','btn_server_down2.png'], max_wait=20)

           if rpa.end_of_queue_state():
               rpa.wait_and_click(['btn_server_40.png','btn_server_40_2.png'], max_wait=2)
               rpa.wait_and_click(['btn_server_select.png'])

        rpa.restore_queue('start_loop')

def server_44():
    """
    ----------------------------------------------------------------------
    Step: Change to Server 44
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_server.png','btn_server2.png','btn_server3.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_server_change.png'], confidence=0.9)

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_server_44.png'], confidence=0.9)

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_server_select.png'], confidence=0.9)

    

    

def server_50():
    """
    ----------------------------------------------------------------------
    Step: Change to Server 50
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_server.png','btn_server2.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_server_change.png'], confidence=0.9)

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_server_up.png'], max_wait=20)

           if rpa.end_of_queue_state():
               rpa.wait_and_click(['btn_server_50.png','btn_server_50_1.png','btn_server_50_3.png'], confidence=0.7, max_wait=5)
               rpa.wait_and_click(['btn_server_select.png'])

        rpa.restore_queue('start_loop')       
  
def server_90():
    """
    ----------------------------------------------------------------------
    Step: Change to Server 90
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_server.png','btn_server2.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_server_change.png'], confidence=0.9)

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_server_up.png'], max_wait=20)

           if rpa.end_of_queue_state():
               rpa.wait_and_click(['btn_server_90.png'], max_wait=1)
               rpa.wait_and_click(['btn_server_select.png'])

        rpa.restore_queue('start_loop')

    rpa.press('esc', presses=5, interval=0.5)

def daily_bonus():
    """
    ----------------------------------------------------------------------
    Step: get daily bonus
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_daily_bonus.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_daily_bonus_collect.png'], max_wait=5)

    rpa.press('esc', presses=5, interval=0.5)

def soul_atrium():
    """
    ----------------------------------------------------------------------
    Step: get daily soul crystal
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_soul_atrium.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_soul_atrium_claim.png'], max_wait=25)

    rpa.press('esc', presses=5, interval=0.5)

def chest():
    """
    ----------------------------------------------------------------------
    Step: open chest
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_chest2.png', 'btn_chest3.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_chest_open.png','btn_chest_open_german.png'], max_wait=5)

    rpa.press('esc', presses=5, interval=0.5)


def daily_quests():
    """
    ----------------------------------------------------------------------
    Step: cleanup daily quests
    ----------------------------------------------------------------------
    """

    rpa.wait_and_click(['btn_daily_quests.png'])

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_quest_complete3.png'], max_wait=5)

    rpa.press('esc', presses=5, interval=0.5)


def airship():
    """
    ----------------------------------------------------------------------
    Step: get all airship tasks
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_airship7.png','btn_airship6.png','btn_airship.png', 'btn_airship2.png','btn_airship3.png','btn_airship4.png','btn_airship5.png'],confidence=0.9)

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['gift_valkyrie.png'])

        if rpa.end_of_queue_state():
            rpa.press('esc', presses=1)

        rpa.wait_and_click(['btn_expeditions_rd.png','btn_expeditions_rd2.png'])

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_with_rd.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_airship_start.png','btn_airship_collect.png'])

                if rpa.end_of_queue_state():
                    rpa.wait_and_click(['btn_airship_auto.png'])
                    rpa.wait_and_click(['btn_airship_start2.png','btn_airship_collect.png'])

                # need to set queue state to start of loop
                rpa.restore_queue('start_loop')

            rpa.press('esc', presses=1)

        rpa.press('esc', presses=5, interval=0.5)

def arena():
    """
    ----------------------------------------------------------------------
    Step: 1st fight in arena
    ----------------------------------------------------------------------
    """
    counter = 0
    max_counter = 10

    rpa.wait_and_click(['btn_arena6.png','btn_arena.png', 'btn_arena2.png','btn_arena3.png', 'btn_arena4.png','btn_arena5.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state() and counter < max_counter:
        rpa.wait_and_click(['btn_kattegat.png','btn_kattegat2.png','btn_schweizer.png'])

        if rpa.end_of_queue_state():
            rpa.sleep(2)
            rpa.press('esc')
            rpa.wait_and_click(['btn_arena_refresh.png'])
            counter += 1
            if counter > max_counter:
                rpa.press('esc', presses=5, interval=0.5)    

            rpa.restore_queue('start_loop')

    rpa.wait_and_click(['btn_arena_attack.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_arena_battle.png','btn_arena_battle2.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_arena_pause.png'], max_wait=20)

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_arena_skip_battle.png'])

    rpa.sleep(5) 
            
    rpa.press('esc', presses=5, interval=0.5)

def arena2():
    """
    ----------------------------------------------------------------------
    Step: 2nd fight in arena
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_arena.png'])

    for i in range(10):
        if rpa.image_found('C:/Users/Torsten Rahmann/rpa/tmp/btn_kattegat.png'):
            pyautogui.click(['btn_arena_refresh.png'])
            break
        else:
            rpa.wait_and_click(['btn_arena_attack.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_arena_battle.png'])

                if rpa.end_of_queue_state():
                    rpa.wait_and_click(['btn_arena_pause.png'], max_wait=20)

                    if rpa.end_of_queue_state():
                        rpa.wait_and_click(['btn_arena_skip_battle.png'])
        pass

             
    rpa.press('esc', presses=5, interval=0.5)

def grand_arena():
    """
    ----------------------------------------------------------------------
    Step: 1 fight in grand arena
    ----------------------------------------------------------------------
    """
    counter = 0
    max_counter = 5

    rpa.wait_and_click(['btn_grand_arena.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_grand_arena_battle.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_schweizer.png','btn_kattegat.png','btn_kattegat2.png','btn_arena_skoll.png','btn_libertalia.png','btn_nullplan.png'])

        if rpa.end_of_queue_state():
            rpa.press('esc')
            rpa.wait_and_click(['btn_grand_arena_refresh.png'])
            counter += 1
            if counter > max_counter:
                rpa.press ('esc', presses=5, interval=0.5)    

            rpa.restore_queue('start_loop')

    rpa.wait_and_click(['btn_grand_arena_attack.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_grand_arena_next.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_grand_arena_next.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_grand_arena_battle2.png'])

                if rpa.end_of_queue_state():
                    rpa.wait_and_click(['btn_grand_arena_pause.png'], max_wait=20)

                    if rpa.end_of_queue_state():
                        rpa.wait_and_click(['btn_grand_arena_skip.png'])

    rpa.press('esc', presses=5, interval=0.5)
       
def send_presents():
    """
    ----------------------------------------------------------------------
    Step: get all airship tasks
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_gifts.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_gifts_send.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_gifts_send_presents.png'], max_wait=5)

            rpa.press('esc', presses=1)

        rpa.press('esc', presses=5, interval=0.5)


def outland():
    """
    ----------------------------------------------------------------------
    Step: get all outland challenges
    """
    rpa.wait_and_click(['btn_outland.png','btn_outland2.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_outland_reward_rd.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_outland_chests.png'])
            rpa.wait_and_click(['btn_outland_open2.png'])
            rpa.wait_and_click(['btn_outland_exit.png'])
            rpa.wait_and_click(['btn_outland_next.png'])

            rpa.restore_queue('start_loop')

    rpa.wait_and_click(['btn_outland_exit.png'])

    rpa.press('esc', presses=5, interval=0.5)

def mail():
    """
    ----------------------------------------------------------------------
    Step: get all mails
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_mail.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_mail_collect_all.png'], max_wait=15)

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_mail_collect_all2.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_mail_show_all.png'], max_wait=15)

        rpa.press('esc', presses=5, interval=0.5)

def tower():
    """
    ----------------------------------------------------------------------
    Step: get all tower chests (without emeralds)
    """
    rpa.wait_and_click(['btn_tower.png','btn_tower2.png','btn_tower3.png'])

    rpa.save_queue('start_loop')

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_tower_instclear.png','btn_tower_instclear2.png'])

        if rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_tower_ch_chests.png'])

        rpa.restore_queue('start_loop')

        while rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_tower_chest.png', 'btn_tower_chest_2.png', 'btn_tower_chest_3.png'], confidence =0.7)
        
           if rpa.end_of_queue_state():
               rpa.wait_and_click(['btn_tower_open.png'])

               if rpa.end_of_queue_state():
                   rpa.wait_and_click(['btn_tower_proceed.png'])
    
    rpa.press('esc', presses=1) # End of tower

    rpa.wait_and_click(['btn_tower_skull.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_tower_exch_skull_coins.png'])

        if rpa.end_of_queue_state():
            rpa.press('esc', presses=1) # Exit collecting coins

    rpa.wait_and_click(['btn_tower_points.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_tower_points_collect.png'])
    
        if rpa.end_of_queue_state():
            rpa.press('esc', presses=1) # Exit collecting points


    rpa.press('esc', presses=5, interval=0.5) # Exit collecting points

def dungeon():
    """
    ----------------------------------------------------------------------
    Step: get oracle cards
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_dungeon.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_dungeon_portal.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_oracle_rd.png'])

            while rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_oracle_claim.png'])

            rpa.wait_and_click(['btn_outland_exit.png'])

        rpa.press('esc', presses=2, interval=0.5)

def divination_cards():
    """
    ----------------------------------------------------------------------
    Step: Use all divination cards
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_dungeon.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_dungeon_portal.png'])

        while rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_divination_battle.png','btn_divination_battle2.png','btn_divination_battle3.png','btn_divination_attack.png','btn_divination_fate.png','btn_divination_fate2.png','btn_divination_savepoint.png','btn_divination_savepoint2.png','btn_divination_collect.png'], max_wait=15)

        rpa.press('esc', presses=6, interval=0.5)

        
    

def tournament():
    """
    ----------------------------------------------------------------------
    Step: Raid tournament
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_titan_valley.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_tournament.png','btn_tournament2.png'], confidence=0.7)

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_tournament_raid.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_tournament_raid2.png'])

                if rpa.end_of_queue_state():
                    rpa.wait_and_click(['btn_tournament_ok.png'])

                    if rpa.end_of_queue_state():
                        rpa.wait_and_click(['btn_tournament_claim.png'])
                   

                # need to set queue state to start of loop
        rpa.restore_queue('start_loop')

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_tournament_chest.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_tournament_claim2.png'])

                
    rpa.press('esc', presses=4, interval=0.5)

        

def altar():
    """
    ----------------------------------------------------------------------
    Step: Open Titan Artifact Sphere
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_titan_valley.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_altar.png','btn_altar2.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_altar_sphere.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_altar_exit.png'])

        rpa.press('esc', presses=5, interval=0.5)

def astral_seer ():

    rpa.wait_and_click(['btn_asgard.png'])

    if rpa.end_of_queue_state():
        # Substep: Cradle of the Stars

        rpa.wait_and_click(['btn_asgard_seer.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_asgard_seer_open.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_outland_exit.png'])

            rpa.press('esc', presses=5, interval=0.5)

def asgard_old():
    """
    # ----------------------------------------------------------------------
    # Step: Asgard
    # ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_asgard.png'])

    if rpa.end_of_queue_state():
        # Substep: Cradle of the Stars

        rpa.wait_and_click(['btn_asgard_seer.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_asgard_seer_open.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_outland_exit.png'])

            rpa.press('esc', presses=5, interval=0.5)

    # Substep: Guild Raid

    rpa.wait_and_click(['btn_asgard_guild_raid.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_asgard_guild_raid_sk1.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_asgard_guild_raid_start.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_asgard_guild_raid_battle.png'])

                # wait for auto battle button
                rpa.wait_for_image(['btn_battle_auto.png'], max_wait=15)

                if rpa.end_of_queue_state():
                    rpa.press('esc', presses=1)

                    rpa.wait_and_click(['btn_asgard_guild_raid_skip.png'])
                    rpa.wait_and_click(['btn_asgard_guild_raid_ok.png'])

            rpa.restore_queue('start_loop')

    rpa.restore_queue('start_loop')

    # while rpa.end_of_queue_state():
    #     rpa.wait_and_click(['btn_asgard_guild_raid_sk2.png', 'btn_asgard_guild_raid_sk3.png'])

    #     while rpa.end_of_queue_state():
    #         rpa.wait_and_click(['btn_asgard_guild_raid_start.png'])

    #         while rpa.end_of_queue_state():
    #             rpa.wait_and_click(['btn_asgard_guild_raid_next.png', 'btn_asgard_guild_raid_battle.png', 'btn_asgard_guild_raid_next2.png'])

    #         rpa.save_queue('start_fights')

    #         while rpa.end_of_queue_state():
    #             # wait for auto battle button
    #             rpa.wait_for_image(['btn_battle_auto.png'], max_wait=15)

    #             if rpa.end_of_queue_state():
    #                rpa.press('esc', presses=1)

    #                rpa.wait_and_click(['btn_asgard_guild_raid_skip.png'])

    #                while rpa.end_of_queue_state():
    #                    rpa.wait_and_click(['btn_asgard_guild_raid_ok.png','btn_asgard_guild_raid_next2.png'])

    #                rpa.restore_queue('start_fights')

    #         rpa.restore_queue('start_loop')

    # after we finished all the steps
    rpa.press('esc', presses=3, interval=0.5)

def asgard():

    rpa.wait_and_click(['btn_asgard.png'])

    rpa.wait_and_click(['btn_asgard_guild_raid.png','btn_asgard_guild_raid2.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_asgard_guild_raid_pause2.png','btn_asgard_guild_raid_sk1.png','btn_asgard_guild_raid_sk2.png', 'btn_asgard_guild_raid_sk3.png','btn_asgard_guild_raid_start.png','btn_asgard_guild_raid_next.png', 'btn_asgard_guild_raid_battle.png', 'btn_asgard_guild_raid_next2.png', 'btn_asgard_guild_raid_battle2.png','btn_asgard_guild_raid_battle_pause.png','btn_asgard_guild_raid_skip.png','btn_asgard_guild_raid_skip2.png','btn_asgard_guild_raid_auto.png','btn_asgard_guild_raid_ok.png'], confidence=0.8)

        rpa.save_queue('start_loop')

    rpa.restore_queue('start_loop')

    rpa.press('esc', presses=3, interval=0.5)

def switch_to_guild():
    """
    ----------------------------------------------------------------------
    Step: switch to guild plane
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_guild.png','btn_guild2.png'])

    # wait until  new plane is displayed
    if rpa.end_of_queue_state():
        rpa.wait_for_image(['btn_to_city.png','btn_to_city2.png'], max_wait=30)


def switch_to_city():
    """
    ----------------------------------------------------------------------
    Step: switch to city plane
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_to_city.png','btn_to_city2.png'])

    # wait until  new plane is displayed
    if rpa.end_of_queue_state():
        rpa.wait_for_image(['btn_guild.png','btn_guild2.png'], max_wait=30)


class CustomLogRecord(logging.LogRecord):
    """ Improve log output for source file and line number """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.origin = f"{self.filename}:{self.lineno}"

def main(ini_file, profile, checksum):
    """ main routine """
    global rpa

    logger.info('RPA client version: %s', checksum)

    app_cfg = load_config(ini_file)
#   tmp_dir = app_cfg['Environment']['tmp_dir']

    rpa = Robotic_Process_Automation(
        name='herowars',
        tmp_dir=app_cfg['Environment']['tmp_dir'],
        scale=float(app_cfg['Environment']['scale']),
        max_wait=float(app_cfg['Environment']['max_wait'])
        )

    # set_tmp_dir(app_cfg['Environment']['tmp_dir'])
    # set_def_scale(float(app_cfg['Environment']['scale']))
    # set_def_max_wait(float(app_cfg['Environment']['max_wait']))

    # init_queue()

    #first_screen()
    #chest()
    #daily_quests()
    #airship()
    #send_presents()
    #outland()
    #mail()
    #switch_to_guild()
    #dungeon()
    #asgard()
    #switch_to_city()
    #daily_quests()

    # repeatable steps, switched to ini file configuration
    for module in app_cfg[profile]["run_daily"].strip().split("\n"):
        globals()[module]()

if __name__ == "__main__":
    RPA_LOGLEVEL = os.environ.get('RPA_LOGLEVEL', 'DEBUG').upper()

    app_chksum = gen_checksum('rpa.py')

    # parse parameters
    parser = argparse.ArgumentParser(description='HW Robot Client')
    parser.add_argument('--version' , action='version', version='%(prog)s rel 1.0.0 (' + app_chksum[0:8] + ')')
    parser.add_argument('--ini-file', required=True, help='Initial parameters file')
    parser.add_argument('--profile', required=True, help='RPA Profile (RPA_<namer>)')
    args = parser.parse_args()

    # setup logging capabilities
    logging.setLogRecordFactory(CustomLogRecord)
    logging.basicConfig(
        format='%(asctime)s [%(origin)-20s] %(levelname)-5s - %(funcName)-20s - %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S',
        level=RPA_LOGLEVEL
        )

    main(args.ini_file, args.profile, app_chksum)
