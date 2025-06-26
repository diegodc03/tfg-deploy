

######################################################################################
# Eliminar el partido de la base de datos
#
# connection:     Conexión con la base de datos
# match_id:       ID del partido
#
######################################################################################
def delete_football_match(spark, jdbc_url, db_properties, match_id):
    
    try:
        query = f"DELETE FROM football_match WHERE match_id = {match_id}"

        # Conectar y ejecutar la consulta
        conn = spark._sc._jvm.java.sql.DriverManager.getConnection(jdbc_url, db_properties["user"], db_properties["password"])
        stmt = conn.createStatement()
        stmt.executeUpdate(query)
        stmt.close()
        conn.close()

        print(f"Match {match_id} deleted successfully.")

    except Exception as e:
        print(f"Error deleting match {match_id}: {e}")


