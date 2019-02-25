from nameko.standalone.rpc import ClusterRpcProxy
import pandas as pd

config = {
    'AMQP_URI': 'amqp://guest:guest@localhost:5672/'
}

def load_hd_file():

    hd_df = pd.read_csv('files/2016/hd2016.csv', encoding='latin1')
    # freq_df = pd.read_csv('files/2016/hd2016-Frequencies.csv')
    # staff_df = pd.read_csv('files/2015/s2015_oc.csv')
    # tuition_df = pd.read_csv('files/2016/ic2016_ay.csv')

    # only active schools
    # only schools that offer four-year degrees
    hd_df = hd_df[(hd_df['ACT'].str.match('A')) & (hd_df['ICLEVEL'] == 1)]

    for index, row in hd_df.iterrows():
        college = {}
        college['UNITID'] = str(row['UNITID'])
        college['INSTNM'] = str(row['INSTNM'])
        college['ADDR'] = str(row['ADDR'])
        college['CITY'] = str(row['CITY'])
        college['STABBR'] = str(row['STABBR'])
        college['GENTELE'] = str(row['GENTELE'])
        college['WEBADDR'] = str(row['WEBADDR'])
        college['ADMINURL'] = str(row['ADMINURL'])
        college['APPLURL'] = str(row['APPLURL'])
        college['NPRICURL'] = str(row['NPRICURL'])
        college['LONGITUD'] = str(row['LONGITUD'])
        college['LATITUDE'] = str(row['LATITUDE'])
        college['SECTOR'] = str(row['SECTOR'])
        college['HBCU'] = str(row['HBCU'])
        college['LOCALE'] = str(row['LOCALE'])
        #print(row['INSTNM'] + ' ' + str(row['INSTSIZE']) + ' ' + str(row['ICLEVEL']))
        with ClusterRpcProxy(config) as cluster_rpc:
            data = cluster_rpc.college_service.process_college(college)
            print(data)

if __name__ == '__main__':
    load_hd_file()