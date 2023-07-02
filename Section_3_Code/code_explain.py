from code_assistance import CodeAssitance
CA = CodeAssitance()

CA.explain(
    """
def write_preparation_data(self, df, output_path ,current_date, current_hour):

        s3_dir = f"{output_path}/day={current_date}/hour={current_hour}/"
        gs_dir = s3_dir.replace("S3", "gs").replace("prod-", "dt-")

        for directory in [s3_dir, gs_dir]:
            df.write.mode('overwrite').parquet(directory)
            self.log(f'Stored in {directory}')
    """
)
