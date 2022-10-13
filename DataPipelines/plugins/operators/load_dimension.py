from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    append = "append"
    delete = "delete"

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 sql="",
                 mode="",
                 table="",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id=redshift_conn_id
        self.sql=sql
        self.mode=mode
        self.table=table

    def execute(self, context):
        self.log.info('LoadDimensionOperator executing ...')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        if self.mode == self.append:
            sql = self.sql
        elif self.mode == self.delete:
            sql = "DELETE FROM {}".format(self.table)
        redshift.run(sql)
        self.log.info("LoadDimensionOperator completed!")
