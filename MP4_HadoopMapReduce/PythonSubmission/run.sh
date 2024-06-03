# A, B
hadoop fs -rm -r -f /MP4_HadoopMapReduce_Template/PythonTemplate/preA-output_Python
hadoop fs -rm -r -f /MP4_HadoopMapReduce_Template/PythonTemplate/A-output_Python
hadoop fs -rm -r -f /MP4_HadoopMapReduce_Template/PythonTemplate/B-output_Python
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files TitleCountMapper.py,TitleCountReducer.py -mapper 'TitleCountMapper.py stopwords.txt delimiters.txt' -reducer 'TitleCountReducer.py' -input dataset/titles/ -output ./preA-output_Python
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files TopTitlesMapper.py,TopTitlesReducer.py -mapper 'TopTitlesMapper.py' -reducer 'TopTitlesReducer.py' -input ./preA-output_Python/ -output ./A-output_Python
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files TopTitleStatisticsMapper.py,TopTitleStatisticsReducer.py -mapper 'TopTitleStatisticsMapper.py' -reducer 'TopTitleStatisticsReducer.py' -input ./A-output_Python/ -output ./B-output_Python


# C
hadoop fs -rm -r -f /MP4_HadoopMapReduce_Template/PythonTemplate/C-output_Python
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files OrphanPagesMapper.py,OrphanPagesReducer.py -mapper 'OrphanPagesMapper.py' -reducer 'OrphanPagesReducer.py' -input dataset/links/ -output ./C-output_Python


# D
hadoop fs -rm -r -f /MP4_HadoopMapReduce_Template/PythonTemplate/linkCount-output_Python
hadoop fs -rm -r -f /MP4_HadoopMapReduce_Template/PythonTemplate/D-output_Python
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files LinkCountMapper.py,LinkCountReducer.py -mapper 'LinkCountMapper.py' -reducer 'LinkCountReducer.py' -input dataset/links/ -output ./linkCount-output_Python
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files TopPopularLinksMapper.py,TopPopularLinksReducer.py -mapper 'TopPopularLinksMapper.py' -reducer 'TopPopularLinksReducer.py' -input ./linkCount-output_Python -output ./D-output_Python


# E
hadoop fs -rm -r -f /MP4_HadoopMapReduce_Template/PythonTemplate/E-output_Python
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files PopularityLeagueMapper.py,PopularityLeagueReducer.py -mapper 'PopularityLeagueMapper.py dataset/league2.txt' -reducer 'PopularityLeagueReducer.py' -input ./linkCount-output_Python -output ./E-output_Python
