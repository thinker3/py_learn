#coding=utf-8
'''
作者： chenkun@etime.net.cn
创建日期： 2013-11-29

退货,财务付款,报关询问 新增表或新增字段用到的脚本

jiayou3 数据表每天都会被覆盖，所以在使用前可能需要运行此脚本
在测试或上线前需要运行此脚本

'''

import MySQLdb,sys,datetime
#HOST='127.0.0.1'
HOST='192.168.0.6'
USER_NAME='lidongdev'
DB_PASSWORD='asdasd'
class ChangeDB(object):
    '''
    '''
    def __init__(self, db_name):
        self.conn = MySQLdb.connect(host=HOST,port=3306, user=USER_NAME,
            passwd=DB_PASSWORD, db=db_name, charset='utf8')
        self.cursor = self.conn.cursor()
        self.db_name = db_name

    def is_table_exists(self, table_name):
        '''
            if the table exits, return 1, else return 0
        '''
        sql = "SHOW TABLES LIKE '%s'" % table_name
        result = self.cursor.execute(sql)
        return result

    def is_column_exists(self, table_name, column_name):
        '''
            if the table not exits, return 1, be careful
            if the column exits, return 1, else return 0
        '''
        if not self.is_table_exists(table_name):
            return 1
        db_name = self.db_name
        sql = '''
                SELECT COLUMN_NAME
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE table_schema = '%s'
                AND table_name = '%s'
                AND column_name = '%s'
            ''' % (db_name, table_name, column_name)
        result = self.cursor.execute(sql)
        return result

    def allocate(self):
        '''
                ON UPDATE CASCADE
                ON DELETE CASCADE
        '''
        # sale_allocatehistory sale_order_id字段 修改为允许为空
        # Columns are nullable by default. As long as the column is not declared UNIQUE or NOT NULL
        sql = '''
                ALTER TABLE sale_allocatehistory MODIFY sale_order_id int(11);
            '''
        self.cursor.execute(sql)

        if not self.is_column_exists('sale_allocatehistory', 'origin'):
            sql = '''
                    ALTER TABLE `sale_allocatehistory` ADD COLUMN `origin` VARCHAR(500);
                '''
            self.cursor.execute(sql)
        if not self.is_column_exists('sale_allocatehistory', 'allocate_time'):
            sql = '''
                    ALTER TABLE `sale_allocatehistory` ADD COLUMN `allocate_time` datetime DEFAULT NULL;
                '''
            self.cursor.execute(sql)
        if not self.is_column_exists('sale_allocatehistory', 'allocator_id'):
            sql = '''
                    ALTER TABLE `sale_allocatehistory` ADD COLUMN `allocator_id` int(11);
                '''
            self.cursor.execute(sql)
            sql = '''
                    ALTER TABLE sale_allocatehistory 
                    ADD CONSTRAINT FK_allocator_user
                    FOREIGN KEY (allocator_id) REFERENCES auth_user(id)
                '''
            self.cursor.execute(sql)

    def goods_return(self):
        '''
        '''
        if not self.is_column_exists('stock_stockpicking', 'is_return'):
            sql = '''
                    ALTER TABLE `stock_stockpicking` ADD COLUMN `is_return` tinyint(1) DEFAULT 0;
                '''
            self.cursor.execute(sql)

    def crm_partner(self):
        '''
        '''
        if not self.is_column_exists('crm_partner', 'default_contact'):
            sql = '''
                    ALTER TABLE `crm_partner` ADD COLUMN `default_contact` int(11);
                '''
            self.cursor.execute(sql)

    def sale_refund(self):
        '''
        '''
        if not self.is_column_exists('sale_salerefund', 'reference_type'):
            sql = '''
                    ALTER TABLE `sale_salerefund` ADD COLUMN `reference_type` VARCHAR(20);
                '''
            self.cursor.execute(sql)

    def custom_quote(self):
        '''
        '''
        db_name = 'sale_customquote'
        column_name = 'sale_quote_id'
        if not self.is_column_exists(db_name, column_name):
            sql = '''
                    ALTER TABLE `%s` ADD COLUMN `%s` int(11);
                ''' % (db_name, column_name)
            self.cursor.execute(sql)
            sql = '''
                    ALTER TABLE sale_customquote 
                    ADD CONSTRAINT FK_custom_quote_sale_quote
                    FOREIGN KEY (sale_quote_id) REFERENCES sale_salequote(id)
                '''
            self.cursor.execute(sql)

        column_name = 'p_name'
        if not self.is_column_exists(db_name, column_name):
            sql = '''
                    ALTER TABLE `%s` ADD COLUMN `%s` VARCHAR(100);
                ''' % (db_name, column_name)
            self.cursor.execute(sql)

        column_name = 'pdf'
        if not self.is_column_exists(db_name, column_name):
            sql = '''
                    ALTER TABLE `%s` ADD COLUMN `%s` VARCHAR(255);
                ''' % (db_name, column_name)
            self.cursor.execute(sql)

    def approvee(self):
        '''
        '''
        sql = """
        CREATE TABLE IF NOT EXISTS `approvals_shiporderpayment` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
            `create_time` datetime NOT NULL,
              `create_user_id` int(11) NOT NULL,
                `write_time` datetime DEFAULT NULL,
                  `write_user_id` int(11) DEFAULT NULL,
                    `money` decimal(18,4) DEFAULT NULL,
                      `desp` varchar(500) DEFAULT NULL,
                        `origin_id` int(11) NOT NULL,
                          `approved` tinyint(1) DEFAULT NULL,
                            PRIMARY KEY (`id`),
                              KEY `approvals_shiporderpayment_b22fdd0f` (`create_user_id`),
                                KEY `approvals_shiporderpayment_b3d26e03` (`write_user_id`),
                                  KEY `approvals_shiporderpayment_bd654448` (`origin_id`)
                                  ) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
        """
        self.cursor.execute(sql)

        sql2 = """
            CREATE TABLE IF NOT EXISTS `approvals_custompayment` (
              `id` int(11) NOT NULL AUTO_INCREMENT,
                `create_time` datetime NOT NULL,
                  `create_user_id` int(11) NOT NULL,
                    `write_time` datetime DEFAULT NULL,
                      `write_user_id` int(11) DEFAULT NULL,
                        `money` decimal(18,4) DEFAULT NULL,
                          `desp` varchar(500) DEFAULT NULL,
                            `origin_id` int(11) NOT NULL,
                              `approved` tinyint(1) DEFAULT NULL,
                                PRIMARY KEY (`id`),
                                  KEY `approvals_custompayment_b22fdd0f` (`create_user_id`),
                                    KEY `approvals_custompayment_b3d26e03` (`write_user_id`),
                                      KEY `approvals_custompayment_bd654448` (`origin_id`)
                                      ) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;
        """
        self.cursor.execute(sql2)

        column_name = 'approved'
        for db_name in ['approvals_shiporderpayment', 'approvals_custompayment']:
            if not self.is_column_exists(db_name, column_name):
                sql = '''
                        ALTER TABLE `%s` ADD COLUMN `%s` tinyint(1);
                    ''' % (db_name, column_name)
                self.cursor.execute(sql)

    def close(self):
        self.cursor.close()
        self.conn.close()
    

def main(db_name):
    """
    """
    obj = ChangeDB(db_name)
    print(1)
    obj.allocate()
    print(2)
    obj.goods_return()
    print(3)
    obj.approvee()
    print(4)
    obj.sale_refund()
    print(5)
    obj.crm_partner()
    print(6)
    obj.custom_quote()
    print(7)
    obj.close()
    print('%s done' % db_name)

def test_is_column_exists():
    obj = ChangeDB('jiayou3')
    print(obj.is_column_exists('auth_user', 'username'))
    print(obj.is_column_exists('auth_user', 'email'))
    print(obj.is_column_exists('auth_user', 'name'))
    obj.close()

def test_is_table_exists():
    obj = ChangeDB('jiayou3')
    print(obj.is_table_exists('auth_user'))
    print(obj.is_table_exists('auth_abc'))
    print(obj.is_table_exists('approvals_shiporderpayment'))
    obj.close()

if __name__=='__main__':
    main('jiayou3')
    main('jiayoutest')
    #main('jiayou3test')
    #test_is_column_exists()
    #test_is_table_exists()
    sys.exit(0)




