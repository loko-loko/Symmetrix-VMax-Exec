# -*- coding: utf-8 -*-

#================================================================================#
# ------------------------------- IMPORT LIBRARY ------------------------------- #
#================================================================================#

#~~~~# LOCAL LIBRARY #~~~~#

from py_vmax_lib.func_global import *
from py_vmax_lib.func_retrieve import *

#============================================================================#
# ------------------------------- DICT VALUE ------------------------------- #
#============================================================================#

opts_dic_lst = [
    { 'actv':False, 'name':'select',       'cat':'mode',  'opt':['select', '-x'],     'msg':'Select Mode',                           'arg':False, 'a_sep':False, 'type':'sl', 'default':False },
    { 'actv':False, 'name':'audit',        'cat':'mode',  'opt':['info', '-i'],       'msg':'Audit Mode',                            'arg':False, 'a_sep':False, 'type':'ad', 'default':False },
    { 'actv':False, 'name':'remove',       'cat':'mode',  'opt':['remove', '-r'],     'msg':'Remove Mode',                           'arg':False, 'a_sep':False, 'type':'rm', 'default':False },
    { 'actv':False, 'name':'create',       'cat':'mode',  'opt':['create', '-c'],     'msg':'Create Mode',                           'arg':False, 'a_sep':False, 'type':'cr', 'default':False },
    { 'actv':False, 'name':'modify',       'cat':'mode',  'opt':['modify', '-m'],     'msg':'Modify Mode',                           'arg':False, 'a_sep':False, 'type':'md', 'default':False },
    { 'actv':False, 'name':'migrate',      'cat':'mode',  'opt':['migrate', '-mig'],  'msg':'Migrate Mode',                          'arg':False, 'a_sep':False, 'type':'mi', 'default':False },
    { 'actv':False, 'name':'help',         'cat':False,   'opt':['-help', '-h'],      'msg':'Help',                                  'arg':False, 'a_sep':False, 'type':'hp', 'default':False },
    { 'actv':False, 'name':'debug_mode',   'cat':False,   'opt':['-debug'],           'msg':'Debug Mode',                            'arg':False, 'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'verbose_mode', 'cat':False,   'opt':['-verbose', '-v'],   'msg':'Verbose Mode',                          'arg':False, 'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'no_prompt',    'cat':False,   'opt':['-nop'],             'msg':'No Prompt',                             'arg':False, 'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'unbind_mode',  'cat':'dev',   'opt':['-ulun'],            'msg':'Unbind Lun',                            'arg':False, 'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'noport_mode',  'cat':'dev',   'opt':['-nplun'],           'msg':'No Port Lun',                           'arg':False, 'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'force_mode',   'cat':False,   'opt':['-force'],           'msg':'Force Flag',                            'arg':False, 'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'no_break',     'cat':False,   'opt':['-no_break', '-n'],  'msg':'No Break for <-name> Option',           'arg':False, 'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'sid',          'cat':False,   'opt':['-sid'],             'msg':'Bay SID',                               'arg':True,  'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'size_display', 'cat':False,   'opt':['-size', '-sz'],     'msg':'Size Display [cyl|mb|auto] (Df:auto)',  'arg':True,  'a_sep':False, 'type':'gl', 'default':'"auto"'},
    { 'actv':False, 'name':'dev_lun',      'cat':'dev',   'opt':['-lun', '-l'],       'msg':'Lun ID',                                'arg':True,  'a_sep':',',   'type':'gl', 'default':False },
    { 'actv':False, 'name':'dev_lwwn',     'cat':'dev',   'opt':['-luid'],            'msg':'Lun Unique ID',                         'arg':True,  'a_sep':',',   'type':'gl', 'default':False },
    { 'actv':False, 'name':'dev_sg',       'cat':'dev',   'opt':['-sg', '-s'],        'msg':'S.Group',                               'arg':True,  'a_sep':',',   'type':'gl', 'default':False },
    { 'actv':False, 'name':'dev_wwn',      'cat':'dev',   'opt':['-wwn', '-w'],       'msg':'Login (WWN)',                           'arg':True,  'a_sep':',',   'type':'gl', 'default':False },
    { 'actv':False, 'name':'tmpsg_mode',   'cat':'dev',   'opt':['-tmpsg'],           'msg':'Info|Remove Tmp S.Group (Total)',       'arg':True , 'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'new_name',     'cat':False,   'opt':['-name'],            'msg':'New Name',                              'arg':True,  'a_sep':False, 'type':'gl', 'default':False },
    { 'actv':False, 'name':'new_sg',       'cat':False,   'opt':['-nsg'],             'msg':'New S.Group',                           'arg':False, 'a_sep':False, 'type':'cr', 'default':False },
    { 'actv':False, 'name':'new_lun',      'cat':False,   'opt':['-nlun'],            'msg':'New Lun',                               'arg':True,  'a_sep':',',   'type':'cr', 'default':False },
    { 'actv':False, 'name':'new_view',     'cat':False,   'opt':['-nview'],           'msg':'New M.View',                            'arg':True,  'a_sep':'-',   'type':'cr', 'default':False },
    { 'actv':False, 'name':'node',         'cat':False,   'opt':['-node'],            'msg':'Node Count (Df:1)',                     'arg':True,  'a_sep':False, 'type':'cr', 'default':1     },
    { 'actv':False, 'name':'rmv_total',    'cat':False,   'opt':['-total', '-t'],     'msg':'Total Remove',                          'arg':False, 'a_sep':False, 'type':'rm', 'default':False },
    { 'actv':False, 'name':'rmv_repli',    'cat':False,   'opt':['-repli', '-rep'],   'msg':'Only Replication Remove',               'arg':False, 'a_sep':False, 'type':'rm', 'default':False },
    { 'actv':False, 'name':'only_mode',    'cat':False,   'opt':['-only', '-o'],      'msg':'Display Only Device Info',              'arg':False, 'a_sep':False, 'type':'ad', 'default':False },
    { 'actv':False, 'name':'flag_mode',    'cat':'modif', 'opt':['-flag', '-f'],      'msg':'Flag to Modify [BCV|SRDF]',             'arg':True,  'a_sep':False, 'type':'md', 'default':False },
    { 'actv':False, 'name':'rmt_new_sg',   'cat':False,   'opt':['-rnsg'],            'msg':'Remote New S.Group',                    'arg':False, 'a_sep':False, 'type':'mi', 'default':False },
    { 'actv':False, 'name':'mig_type',     'cat':False,   'opt':['-mtype'],           'msg':'Migration Type [CLONE|VLUN|SRDF]',      'arg':True,  'a_sep':False, 'type':'mi', 'default':False },
    { 'actv':False, 'name':'rmt_sid',      'cat':False,   'opt':['-rsid'],            'msg':'Remote SID',                            'arg':True,  'a_sep':False, 'type':'mi', 'default':False },
    { 'actv':False, 'name':'rmt_sg',       'cat':False,   'opt':['-rsg'],             'msg':'Remote S.Group',                        'arg':True,  'a_sep':',',   'type':'mi', 'default':False },
    { 'actv':False, 'name':'rmt_lun',      'cat':False,   'opt':['-rlun'],            'msg':'Remote Lun',                            'arg':True,  'a_sep':',',   'type':'mi', 'default':False },
]

lun_size_dic_lst = [
    {'reg' : '5[0-4][0-6][0-9]' , 'cyl_12' : 5948800  , 'cyl_3' : 2974400  , 'size_gb' : 5400  },
    {'reg' : '3[0-4][0-6][0-9]' , 'cyl_12' : 3569280  , 'cyl_3' : 1784640  , 'size_gb' : 3240  },
    {'reg' : '2[0-2][0-7][0-9]' , 'cyl_12' : 2379520  , 'cyl_3' : 1189760  , 'size_gb' : 2160  },
    {'reg' : '10[0-8][0-9]'	    , 'cyl_12' : 1189760  , 'cyl_3' : 594880   , 'size_gb' : 1080  },
    {'reg' : '6[0-5][0-9]'      , 'cyl_12' : 713856   , 'cyl_3' : 356928   , 'size_gb' : 648   },
    {'reg' : '4[0-3][0-9]'      , 'cyl_12' : 475904   , 'cyl_3' : 237952   , 'size_gb' : 432   },
    {'reg' : '3[0-3][0-9]'      , 'cyl_12' : 356928   , 'cyl_3' : 178464   , 'size_gb' : 324   },
    {'reg' : '2[0-1][0-9]'      , 'cyl_12' : 237952   , 'cyl_3' : 118976   , 'size_gb' : 216   },
    {'reg' : '10[0-9]'          , 'cyl_12' : 118976   , 'cyl_3' : 59488    , 'size_gb' : 108   },
    {'reg' : '5[0-9]'           , 'cyl_12' : 59488    , 'cyl_3' : 29744    , 'size_gb' : 54    },
    {'reg' : '2[0-9]'           , 'cyl_12' : 29744    , 'cyl_3' : 14872    , 'size_gb' : 27    },
    {'reg' : '1[0-5]'           , 'cyl_12' : 14872    , 'cyl_3' : 7436     , 'size_gb' : 13    },
    {'reg' : '[6-8]'            , 'cyl_12' : 7436     , 'cyl_3' : 3718     , 'size_gb' : 7     },
    {'reg' : '2'                , 'cyl_12' : 2184     , 'cyl_3' : 1092     , 'size_gb' : 2     },
    {'reg' : '1'                , 'cyl_12' : 1096     , 'cyl_3' : 548      , 'size_gb' : 1     },
    {'reg' : '0'                , 'cyl_12' : 3        , 'cyl_3' : 6        , 'size_gb' : 0     },
]

#==============================================================================#
# ------------------------------- MODULE START ------------------------------- #
#==============================================================================#

# @function_check
def lun_display(sid, lun_cls_lst, array_type, word='', war_type='Warning', err_type='Error', disp_type='Display', wwn_type=False, size_display='auto', debug=False, verbose=False):
    
    total_sum = sum(lun_cls_lst)
    allocate_sum = sum(lun.allocate for lun in lun_cls_lst)
    written_sum = sum(lun.written for lun in lun_cls_lst)
    lun_by_type = lun_by_type_retrieve(lun_cls_lst)
    
    row_title = ['ID', 'Type', 'Size', 'State', 'Pool', 'S.Group', 'Clone', 'SRDF', 'BCV', 'OR']
    row_key = ['id', 'type', 'size_fmt', 'state_fmt', 'pool_name', 'sgroup_list_fmt', 'clone_display', 'srdf_display', 'bcv_display', 'openr_display']
    
    if size_display == 'mb':
        row_title[2] = 'Size[MB]'
        row_key[2] = 'size'
    elif size_display == 'cyl':
        row_title[2] = 'Size[Cyl]'
        row_key[2] = 'size_cyl'
    
    if verbose or wwn_type:
        row_title.insert(1, 'Unique ID')
        row_key.insert(1, 'wwn_id')
        
    if verbose:
        row_title.insert(3, 'Allocat Write')
        row_key.insert(3, 'allocate_written_fmt')
        
    
    mprint('[{0}] Device(s) Information{1}'.format(sid, word), 't1', tbc=2, tac=1)
    
    mprint('Total Size [T.Nb]  : {0} [{1}]'.format(size_conv(total_sum, 'MB', rd=True), len(lun_cls_lst)))
    mprint('Total Allocate     : {0} ({1}%)'.format(size_conv(allocate_sum, 'MB', rd=True), percent_fmt(allocate_sum, total_sum)))
    mprint('Total Written      : {0} ({1}%)'.format(size_conv(written_sum, 'MB', rd=True), percent_fmt(written_sum, total_sum)))
    mprint('Lun By Type        : {0}'.format(','.join(lun_by_type)))
    mprint()
    
    table_display(lun_cls_lst, row_key, row_title, sort_key='sgroup_list,size,type', reverse = True)
    
    device_display_footer(lun_cls_lst, err_type=err_type, war_type=war_type, disp_type=disp_type, debug=debug)
    
    if verbose:
        
        meta_cls_lst = [l for l in lun_cls_lst if l.meta]
        
        if meta_cls_lst:
            mprint('[{0}] Meta(s) Detail{1}'.format(sid, word), 't1', tbc=2, tac=1)
            
            table_display(
                meta_cls_lst,
                ['id', 'meta_count', 'meta_size_fmt', 'meta_list'],
                ['Head', 'Cnt', 'Size', 'Members'],
                sort_key='meta_count',
                color_stx=False,
                reverse = True
            )
        
        srdf_dic_lst = rtr_dict_list(lun_cls_lst, 'srdf_list_info', concat=True)
        
        if srdf_dic_lst:
            mprint('[{0}] SRDF Pair(s) Detail{1}'.format(sid, word), 't1', tbc=2, tac=1)
            
            table_display(
                srdf_dic_lst,
                ['local_dev_name', 'local_type', 'remote_dev_name', 'remote_symid', 'mode', 'pair_state', 'link_status_change_time'],
                ['L.ID', 'L.Type', 'R.ID', 'R.Array', 'Mode', 'State', 'Last Action'],
                sort_key = 'local_dev_name',
                reverse = True,
                cls_mode = False
            )
            
        clone_dic_lst = rtr_dict_list(lun_cls_lst, 'clone_info_dic_lst', concat=True)
        
        if clone_dic_lst:
            mprint('[{0}] Clone Pair(s) Detail{1}'.format(sid, word), 't1', tbc=2, tac=1)
            
            table_display(
                clone_dic_lst,
                ['source_dev_name', 'type', 'target_dev_name', 'percent_copied', 'last_action'],
                ['S.ID', 'L.Type', 'T.ID', 'Cp%', 'Last Action'],
                sort_key = 'source_dev_name',
                reverse = True,
                cls_mode = False
            )
        
        openr_dic_lst = rtr_dict_list(lun_cls_lst, 'openr_dic_lst', concat=True)
        
        if openr_dic_lst:
            mprint('[{0}] Open Replicator Pair(s) Detail{1}'.format(sid, word), 't1', tbc=2, tac=1)
            
            table_display(
                openr_dic_lst,
                ['local_dev', 'session_name', 'state', 'mode', 'percent_copied', 'remote_wwn'],
                ['L.ID', 'Session.N', 'State', 'Mode', 'Cp%', 'R.UID'],
                sort_key = 'session_name',
                reverse = True,
                cls_mode = False
            )
        
        
        
# @function_check
def sgroup_display(sid, sgroup_cls_lst, view_cls_lst, array_type, display_view_info=True, debug=False):
    
    sg_arg = []
    
    mprint('[{0}] S.Group(s) Information'.format(sid), 't1', tbc = 2, tac = 1)
    
    for x, sgroup in enumerate(sgroup_cls_lst):
        sgroup = sgroup.__dict__
        
        if array_type == 12:
            fast_slo = 'Fast Policy'
            
        elif array_type == 3:
            fast_slo = 'Service Lvl. Obj.'
            
        sgroup_name_fmt = sgroup['name']
        
        if sgroup['argument']:
            sgroup_name_fmt = color_str(sgroup_name_fmt, 'rev')
            sg_arg.append(sgroup['name'])
            
        if sgroup['type'] == 'parent':
            sgroup_name_fmt = '[Parent] {0} [C:{1}]'.format(sgroup_name_fmt, ','.join(sgroup['cascad_sgroup_name']))
        
        elif sgroup['type'] == 'child':
            sgroup_name_fmt = '[Child] {0} [P:{1}]'.format(sgroup_name_fmt, ','.join(sgroup['cascad_sgroup_name']))
        
        mprint(' o-> {0:<17} : {1}'.format('Storage Group', sgroup_name_fmt))
        mprint('     {0:<17}'.format('~'*len('Storage Group')))
        mprint('  {0:<20} : {1} [{2}]'.format('Lun T.Size [T.Cnt]', size_conv(sgroup.get('total_size_mb', 0), 'MB', rd=True), sgroup.get('lun_count', 0)))
        mprint('  {0:<20} : {1}'.format(fast_slo, sgroup.get('fast_name', 'No')))
        
        if display_view_info:
        
            if sgroup['view']:
                view_dic_lst = [view.__dict__ for view in view_cls_lst if view.sgroup == sgroup['name']]
                
                for view_dic in view_dic_lst:
                    mprint('  {0:<20} : {1} [{2}]'.format('Masking View [PG]', view_dic['name'], view_dic['pgroup']))
                    
                    if view_dic['init_csc']:
                        mprint('  {0:<20} : {1}'.format(' Casc. Init. Gr.', view_dic['init']))
                        
                        for init_chlid_dic in view_dic['init_child_info']:
                            mprint('  {0:<20} : {1} [{2}]'.format('  IG Child [WWN]', init_chlid_dic['name'], empty_result_fmt('|'.join(init_chlid_dic['login_list']))))
                            
                    else:
                        
                        mprint('  {0:<20} : {1} [{2}]'.format(' Iniator [WWN]', view_dic['init'], empty_result_fmt('|'.join(view_dic['login_list']))))
                
            else:
                mprint('  {0:<20} : No'.format('Masking View'))
            
        else:
            
            if sgroup['view']:
                view_fmt = 'Yes'
            else:
                view_fmt = 'No'
            
            mprint('  {0:<20} : {1}'.format('Masking View', view_fmt))
            
            
        if x != len(sgroup_cls_lst)-1: mprint()
        
    if any([s.argument for s in sgroup_cls_lst]):
        mprint('{0} : S.Group(s) as Argument'.format(color_str('  ', 'rev')), tbc=1)
        
    sg_view_cls_lst = sgroup_cls_lst + view_cls_lst
    device_display_footer(sg_view_cls_lst, debug=debug)
    
# @function_check
def login_display(sid, login_cls_lst, war_type='Warning', debug=False):
    
    mprint('[{0}] Login(s) Information'.format(sid), 't1', tbc=2, tac=1)
    
    table_display(
        login_cls_lst,
        ['wwn', 'port_count', 'node_port_fmt', 'status_log_in', 'status_on_fab', 'status_fcid', 'port_all_dir_prt_list', 'init_cnt_fmt', 'view_cnt_fmt', 'cig_cnt_fmt'],
        ['Name', 'P', 'P.Name', 'Log In', 'On Fab', 'Fcid', 'Port', 'IG[Nb]', 'MV[Nb]', 'CIG'],
        sort_key = 'port_count',
        reverse = True,
    )
    
    device_display_footer(login_cls_lst, war_type=war_type, debug=debug)
    

# @function_check 
def pool_display(sid, pool_cls_lst, lun_total_size, lun_total_consum_size=0, err_type='Not Avail.', war_type='Warn. Limit', disp_type='Current Pool', mode_migrate=False, debug=False):
    
    mprint('[{0}] Pool(s) Information'.format(sid), 't1', tbc=2, tac=1)
    
    row_key = ['name', 'total_fmt', 'used_fmt', 'used_prc', 'subs_prc', 'subs_prc_aft_lun_add_fmt', 'silo_id_cnt', 'silo_used_prc', 'silo_subs_prc']
    row_title = ['Name', 'Size', 'Us' , 'Us%', 'Ov%', 'Ov%[+{0}]'.format(size_conv(lun_total_size, 'GB', rd=True)), 'Silo', 'S.Us%', 'S.Ov%']
    
    if mode_migrate:
        row_key.insert(4, 'prc_aft_lun_add_fmt')
        row_title.insert(4, 'Us%[+{0}]'.format(size_conv(lun_total_consum_size, 'GB', rd=True)))
    
    table_display( 
        pool_cls_lst,    
        row_key,    
        row_title, 
    )    
    
    device_display_footer(pool_cls_lst, err_type=err_type, war_type=war_type, disp_type=disp_type, debug=debug)
    
    
def srp_display(sid, srp_cls_lst, lun_total_size, lun_total_consum_size=0, mode_migrate=False, debug=False):
    
    mprint('[{0}] SRP(s) Information'.format(sid), 't1', tbc=2, tac=1)
    
    row_key = ['name', 'total_fmt', 'used_fmt', 'used_prc', 'subs_prc', 'subs_prc_aft_lun_add_fmt']
    row_title = ['Name', 'Size', 'Us' , 'Us%', 'Ov%', 'Ov%[+{0}]'.format(size_conv(lun_total_size, 'GB', rd=True))]
    
    if mode_migrate:
        row_key.insert(4, 'prc_aft_lun_add_fmt')
        row_title.insert(4, 'Us%[+{0}]'.format(size_conv(lun_total_consum_size, 'GB', rd=True)))
    
    table_display( 
        srp_cls_lst,    
        row_key,    
        row_title, 
    )   
    
    device_display_footer(srp_cls_lst, debug=debug)
    
# @function_check 
def ra_group_display(sid, ra_cls_lst, debug=False):
    
    mprint('[{0}] RA.Group Information'.format(sid), 't1', tbc=2, tac=1)
    
    table_display( 
        ra_cls_lst,    
        ['ra_group_num', 'rmt_ra_group_num', 'rmt_id', 'ra_port_id', 'ra_port_id_count', 'ra_group_label'],    
        ['RA.ID(Local)', 'RA.ID(Remote)', 'Sym.ID(Remote)', 'FA.Port', 'FA.Cnt' , 'Label'], 
    )    
    
    device_display_footer(ra_cls_lst, debug=debug)
    
# @function_check 
def cmd_display_header(mode, error_dict, logger=False):
    
    if mode == 'display':
        title = 'Command(s) To Execute'
    if mode == 'exec':
        title = 'Command(s) Execution Start'
    
    mprint()
    
    if error_dict:
        for error in error_dict.values():
            mprint(error, 'err', exit=False)
        sc_exit(86, logger=logger)
    
    mprint()
    mprint(title, 't1')
    mprint()

# @function_check
def cmd_display_footer(mode, warning_dict, sc_mode, logger=False, start_time='', nop=False):
    
    if mode == 'display':
        if warning_dict:
            for warning in warning_dict.values():
                mprint(warning, 'war', logger=logger, tbc=0)
        
        if not nop:
            mprint()
            choice = text_input('Do you Want Execute Command(s) ?', '[Yes|No]', out_type='bool')
            
            if choice:
                pass
            else:
                logger.warning('[USER:CANCEL] : Execution Cancel by User')
                sc_exit(0, mode=sc_mode, start_time=start_time, logger=logger)
    
def device_display_footer(cls_lst, err_type='Error', war_type='Warning', disp_type='Current', debug=False):
    
    if any([c.display for c in cls_lst]):
        
        display_type_fmt = ' {0} {1}'.format(color_str('  ', 'blu'), disp_type)
        
        mprint()
        mprint('{0:<30} {1}'.format(display_type_fmt, ''))
         
    if any([c.error for c in cls_lst]):
        
        err_type_fmt = ' {0} {1}'.format(color_str('  ', 'red'), err_type)
        error_msg = [c.error_msg for c in cls_lst if c.error_msg]
        
        if error_msg:
            error_msg_fmt = ': {0}'.format(', '.join(error_msg))
        else:
            error_msg_fmt = ''
        
        mprint()
        mprint('{0:<30} {1}'.format(err_type_fmt, error_msg_fmt))
    
    if any([c.warning for c in cls_lst]):
        
        warning_type_fmt = ' {0} {1}'.format(color_str('  ', 'yel'), war_type)
        warning_msg = [c.warning_msg for c in cls_lst if c.warning_msg]
        
        if warning_msg:
            warning_msg_fmt = ': {0}'.format(', '.join(warning_msg))
        else:
            warning_msg_fmt = ''
        
        mprint()
        mprint('{0:<30} {1}'.format(warning_type_fmt, warning_msg_fmt))
        
    debug_fmt(debug, [c.__dict__ for c in cls_lst])
    
    
def opt_display(opt_type, opt_lst):
    mprint(opt_type, 't2', tbc=1)    
    for l in opt_lst:      
        mprint(l)    
        
def help_display(opts_dic_lst, array_dic_lst, verbose):
    
    mprint('|| OPTIONS ||', 't1', tbc=1)
    
    mode_opt_lst = []
    global_opt_lst = []
    audit_opt_lst = []
    create_opt_lst = []
    remove_opt_lst = []
    migrate_opt_lst = []
    modify_opt_lst = []
    
    for o in opts_dic_lst:
        
        if o['arg']:
            v = '{0:<10}{1:<10} : {2}'.format(', '.join(o['opt']), '[Arg]', o['msg'])
        else:
            v = '{0:<20} : {1}'.format(', '.join(o['opt']), o['msg'])
        
        if o['cat'] == 'mode':
            mode_opt_lst.append(v)
        elif o['type'] == 'gl' or o['type'] == 'hp':
            global_opt_lst.append(v)
        elif o['type'] == 'ad':
            audit_opt_lst.append(v)
        elif o['type'] == 'cr':
            create_opt_lst.append(v)
        elif o['type'] == 'rm':
            remove_opt_lst.append(v)
        elif o['type'] == 'mi':
            migrate_opt_lst.append(v)
        elif o['type'] == 'md':
            modify_opt_lst.append(v)
        
    opt_display('General Options', global_opt_lst)
    opt_display('Mode Selection', mode_opt_lst)
    opt_display('Audit Options', audit_opt_lst)
    opt_display('Create Options', create_opt_lst)
    opt_display('Remove Options', remove_opt_lst)
    opt_display('Migrate Options', migrate_opt_lst)
    opt_display('Modify Options', modify_opt_lst)
    
    mprint('|| EXAMPLES ||', 't1', tbc=2)
    
    mprint('Audit Mode', 't2', tbc=1)
    mprint('vmax_utils.py -sid <SID> info -lun <L.ID>')
    mprint('vmax_utils.py -sid <SID> info -sg <SG>')
    mprint('vmax_utils.py -sid <SID> info -wwn <WWN>')
    mprint('vmax_utils.py -sid <SID> info -luid <L.UID>')
    mprint('vmax_utils.py -sid <SID> info -lun <L.ID> -o')
    
    mprint('Create Mode', 't2', tbc=1)
    mprint('vmax_utils.py -sid <SID> create -nlun <N.LUN> -sg <SG>')
    mprint('vmax_utils.py -sid <SID> create -nsg -name <SRV.N> -nlun <N.LUN>')
    mprint('vmax_utils.py -sid <SID> create -nview <WWN> -nsg -name <SRV.N> -nlun <N.LUN>')
    mprint('vmax_utils.py -sid <SID> create -nview [<NODE.N>]<WWN>-[<NODE.N>]<WWN> -sg <SG> -name <SRV.N>')
    mprint()
    mprint('<-nlun> Syntax Examples : 1x54,5x108:2 or 1x1093c,3x7436c:2')
    
    mprint('Remove Mode', 't2', tbc=1)
    mprint('vmax_utils.py -sid <SID> remove -lun <L.ID>')
    mprint('vmax_utils.py -sid <SID> remove -sg <SG>')
    mprint('vmax_utils.py -sid <SID> remove -sg <SG> -total')
    
    mprint('Migrate Mode', 't2', tbc=1)
    mprint('vmax_utils.py -sid <SID> migrate -mtype SRDF -lun <L.ID> -rsid <R.SID> -rsg <RN.NAME>')
    mprint('vmax_utils.py -sid <SID> migrate -mtype SRDF -sg <SG> -rsid <R.SID> -rnsg -name <RN.NAME>')
    mprint('vmax_utils.py -sid <SID> migrate -mtype SRDF -lun <L.ID> -rsid <R.SID> -rlun <RL.ID>')
    mprint('vmax_utils.py -sid <SID> migrate -mtype CLONE -lun <L.ID> -rsg <RN.NAME>')
    mprint('vmax_utils.py -sid <SID> migrate -mtype CLONE -sg <SG> -rnsg -name <RN.NAME>')
    mprint('vmax_utils.py -sid <SID> migrate -mtype CLONE -lun <L.ID> -rlun <RL.ID>')
    mprint('vmax_utils.py -sid <SID> migrate -mtype VLUN -sg <SG>')
    
    mprint('Modify Mode', 't2', tbc=1)
    mprint('vmax_utils.py -sid <SID> modify -flag BCV -lun <L.ID>')
    mprint('vmax_utils.py -sid <SID> modify -flag SRDF -sg <SG>')
    
    if verbose:
        mprint('|| AVAILABLE ARRAY ||', 't1', tbc=2, tac=1)
        table_display(array_dic_lst, ['id', 'type', 'loc', 'export'], ['Array ID', 'Type', 'Location', 'S.Connect'], cls_mode=False, sort_key='loc,type', reverse=True)
        
        mprint('|| AVAILABLE LUNS SIZE ||', 't1', tbc=2, tac=1)
        table_display(lun_size_dic_lst, ['size_gb', 'cyl_12', 'cyl_3'], ['Size GB', 'Cyl Vx1-2', 'Cyl Vx3'], cls_mode=False, reverse=True)
    
    
    