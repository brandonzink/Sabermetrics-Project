select distinctrow e.GAME_ID, e.INN_CT, concat(ros.FIRST_NAME_TX,' ',ros.LAST_NAME_TX) as 'NAME', e.BAT_ID, substring(e.GAME_ID,4,4) as 'Year', e.BASE1_RUN_ID, e.BASE2_RUN_ID, e.BASE3_RUN_ID, e.BAT_DEST_ID, e.RUN1_DEST_ID, 
e.RUN2_DEST_ID, e.RUN3_DEST_ID from events e
join rosters ros on ros.PLAYER_ID = e.BAT_ID
where ERR_CT = 0 and (e.BAT_DEST_ID != 0 or e.RUN1_DEST_ID != 0 or e.RUN2_DEST_ID != 0 or e.RUN3_DEST_ID != 0)
group by e.BAT_ID; #and substring(e.GAME_ID,4,4));

select * from events;