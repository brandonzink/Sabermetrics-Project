select concat(ros.FIRST_NAME_TX,' ',ros.LAST_NAME_TX) as 'NAME', e.BAT_ID as 'Batter ID', substring(e.GAME_ID,4,4) as 'Year', e.OUTS_CT as 'Outs', e.BASE1_RUN_ID as '1B Runner', e.BASE2_RUN_ID as '2B Runner', e.BASE3_RUN_ID as '3B Runner', e.BAT_DEST_ID 'Batter Dest.', e.RUN1_DEST_ID '1B Runner Dest.', 
e.RUN2_DEST_ID as '2B Runner Dest.', e.RUN3_DEST_ID as '3B Runner Dest', e.START_BASES_CD as 'Start Bases', e.END_BASES_CD as 'End Bases', 
e.EVENT_RUNS_CT as 'Event Runs', e.EVENT_OUTS_CT as 'Event Outs' from events e
join rosters ros on ros.PLAYER_ID = e.BAT_ID
where ERR_CT = 0 and (e.BAT_DEST_ID != 0 or e.RUN1_DEST_ID != 0 or e.RUN2_DEST_ID != 0 or e.RUN3_DEST_ID != 0);