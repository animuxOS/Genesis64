/*
* playlist.h -- SMIL definition
* Copyright (C) 2000 Arne Schirmacher <arne@schirmacher.de>
* Copyright (C) 2001-2007 Dan Dennedy <dan@dennedy.org>
*
* This program is free software; you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation; either version 2 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program; if not, write to the Free Software Foundation,
* Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
*/

#ifndef _PLAYLIST_H
#define _PLAYLIST_H

// C++ Include files
#include <vector>
using std::vector;
#include <string>
using std::string;
#include <map>
using std::map;
#include "smiltime.h"

// C includes

#include <libxml/xmlmemory.h>
#include <libxml/parser.h>
#include <time.h>

// forward declarations

class Frame;
class FileHandler;

/** The PlayList class handles a collection of movie files.
*/

class PlayList
{
public:
	PlayList();
	PlayList( const PlayList& );
	PlayList& operator=( const PlayList& );
	~PlayList();

	xmlNodePtr GetBody( ) const;
	int GetNumFrames() const;
	char* GetFileNameOfFrame( int frameNum ) const;
	bool GetFrame( int frameNum, Frame &frame );
	bool GetMediaObject( int frameNum, FileHandler **media );
	int GetClipBegin( int frameNum ) const;
	int GetClipEnd( int frameNum ) const;
	bool SetClipBegin( int frameNum, const char* value );
	bool SetClipEnd( int frameNum, const char* value );
	int FindStartOfScene( int frameNum ) const;
	int FindEndOfScene( int frameNum ) const;
	void AutoSplit( int first, int last );
	bool SplitSceneBefore( int frameNum );
	bool JoinScenesAt( int frameNum );
	bool GetPlayList( int first, int last, PlayList &playlist ) const;
	bool InsertPlayList( PlayList &playlist, int before );
	bool Delete( int first, int last );
	bool LoadMediaObject( char *filename );
	bool LoadPlayList( char *filename );
	bool SavePlayList( char *filename, bool isLegacyFormat = false );
	bool SavePlayListEli( char *filename, bool isPAL );
	bool SavePlayListSrt( const char *filename );
	void CleanPlayList( xmlNodePtr node );
	void CleanPlayList( );
	bool IsFileUsed( string filename ) const;
	bool IsDirty( ) const;
	void SetDirty( bool value );
	string GetDocName( ) const;
	void GetLastCleanPlayList( PlayList &playlist );
	void SetDocName( string );
	string GetProjectDirectory( );
	string GetSeqAttribute( int frameNum, const char* ) const;
	bool SetSeqAttribute( int frameNum, const char*, const char* );
    bool SetDocId( const char* value );
    string GetDocId( ) const;
    bool SetDocTitle( const char* value );
    string GetDocTitle( ) const;
	
protected:
	bool dirty;

private:
	void RefreshCount();
	void AutoSplit( int first, time_t startTime, int last, time_t endTime, int fps );
	string doc_name;
	xmlDocPtr doc;
	int count;
	SMIL::MediaClippingTime time;
};

/** Directory and path utilities
*/

class directory_utils
{
public:
	static string join_file_to_directory( const string directory, const string &file );
	static string get_directory_from_file( const string &file );
	static string get_absolute_path_to_file( const string &directory, const string &file );
	static string get_relative_path_to_file( const string &directory, const string &file );
	static string expand_directory( const string directory );
};

/** The EditorBackup class holds the previous PlayLists for undo/redo functionality.
*/

class EditorBackup
{
private:
	int maxUndos;
	int position;
	vector <PlayList *> backups;
public:
	EditorBackup();
	~EditorBackup();
	void Store( PlayList *, bool isPersisted = true );
	void Undo( PlayList * );
	void Redo( PlayList * );
	void SetAllDirty( );
	void Clear( );
	bool Restore( PlayList * );
};

/** The singleton method for obtaining the instance of the EditorBackup.
*/

extern EditorBackup *GetEditorBackup();


/** The FileMap class holds the mappings between the file name and the loaded file objects.
*/

class FileMap
{
public:
	virtual ~FileMap()
	{ }
	/** The map from file name to handler is here */
	virtual map<string, FileHandler*> &GetMap() = 0;
	/** Clears the content of the file map. */
	virtual void Clear() = 0;
	/** Obtains a list of unused fx rendered files. */
	virtual void GetUnusedFxFiles( PlayList &list, vector< string > &unused ) = 0;
};

/** The singleton method for obtain the instance of the file map.
*/

extern FileMap *GetFileMap( );


#endif
